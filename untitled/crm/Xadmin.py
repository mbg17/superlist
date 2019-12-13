# by luffycity.com
from django.shortcuts import render
from Xadmin.service.Xadmin import site, ModelAdmin
from django.http import JsonResponse
from django.db.models import Q
from .models import *
import datetime

site.register(School)


class UserConfig(ModelAdmin):
    list_display = ["name", "email", "depart"]


site.register(UserInfo, UserConfig)


class ClassConfig(ModelAdmin):

    def display_classname(self, obj=None, is_header=False):
        if is_header:
            return "班级名称"
        class_name = "%s(%s)" % (obj.course.name, str(obj.semester))
        return class_name

    list_display = [display_classname, "tutor", "teachers"]


site.register(ClassList, ClassConfig)

from django.utils.safestring import mark_safe
from django.urls import path

from django.shortcuts import HttpResponse, redirect


class CusotmerConfig(ModelAdmin):
    def public_view(self, request):
        customer_list=Customer.objects.filter(Q(last_consult_date__lt=datetime.datetime.now()-datetime.timedelta(days=15))|Q(recv_date__lt=datetime.datetime.now()-datetime.timedelta(days=3)),status=2)
        return render(request, 'public_view.html', locals())

    def display_gender(self, obj=None, is_header=False):
        if is_header:
            return "性别"
        return obj.get_gender_display()

    def display_course(self, obj=None, is_header=False):
        if is_header:
            return "咨询课程"
        temp = []
        for course in obj.course.all():
            s = "<a href='/Xadmin/crm/customer/cancel_course/%s/%s' style='border:1px solid #369;padding:3px 6px'><span>%s</span></a>&nbsp;" % (
            obj.pk, course.pk, course.name,)
            temp.append(s)
        return mark_safe("".join(temp))

    list_display = ["name", display_gender, display_course, "consultant", ]

    def cancel_course(self, request, customer_id, course_id):
        print(customer_id, course_id)

        obj = Customer.objects.filter(pk=customer_id).first()
        obj.course.remove(course_id)
        return redirect(self.get_list_url())

    def further(self,request,customer_id):
        user_id=1
        ret=Customer.objects.filter(Q(last_consult_date__lt=datetime.datetime.now()-datetime.timedelta(days=15))|Q(recv_date__lt=datetime.datetime.now()-datetime.timedelta(days=3)),status=2,pk=customer_id).update(recv_date=datetime.datetime.now(),last_consult_date=datetime.datetime.now(),consultant=user_id)
        print(ret)
        if not ret:
            return HttpResponse('已有人跟进！')
        FuthurDetail.objects.create(customer_id=customer_id,consultant_id=user_id,date=datetime.datetime.now())
        return HttpResponse('跟进成功！')

    def mycustomer(self,request):
        user_id=1
        futhurDetail=FuthurDetail.objects.filter(consultant_id=user_id).all()
        return render(request, 'mycustomer.html', locals())
    def extra_url(self):
        temp = []
        # 公共客户页面
        temp.append(path("public/", self.public_view))
        # 跟进页面
        temp.append(path("further/<int:customer_id>/", self.further))
        # 取消咨询课程页面
        temp.append(path("cancel_course/<int:customer_id>/<int:course_id>", self.cancel_course))
        # 我的客户
        temp.append(path("mycustomer/", self.mycustomer))
        return temp


site.register(Customer, CusotmerConfig)
site.register(Department)


class StudentConfig(ModelAdmin):
    def score_view(self, request, student_id):
        if request.is_ajax():
            sid = request.GET.get('sid')
            cid = request.GET.get('cid')
            study_record_obj = StudyRecord.objects.filter(student=sid, course_record__class_obj=cid)
            data = []
            for study_record in study_record_obj:
                data.append([f'day{study_record.course_record.day_num}', study_record.score])
            return JsonResponse(data, safe=False)
        time = datetime.datetime.now().strftime('%Y-%m-%d')
        student = Student.objects.filter(id=student_id).first()
        class_list = student.class_list.all()
        return render(request, 'score_view.html', locals())

    def extra_url(self):
        temp = []
        temp.append(path("score_view/<int:student_id>/", self.score_view))
        return temp

    def score_show(self, obj=None, is_header=False):
        if is_header:
            return '查看成绩'
        return mark_safe(f'<a href="score_view/{obj.pk}/">查看成绩</a>')

    list_display = ["username", 'class_list', score_show]


site.register(Student, StudentConfig)
site.register(Course)


class ConsultRecordConfig(ModelAdmin):
    list_display = ["customer", 'date', 'note']


site.register(ConsultRecord, ConsultRecordConfig)


class CourseRecordConfig(ModelAdmin):
    def change_score(self, request, course_id):
        if request.method == 'POST':
            id = request.POST.get('id')
            obj = '没有人'
            for key, value in request.POST.items():
                if key == 'homework_note':
                    obj = StudyRecord.objects.filter(pk=id[0]).update(homework_note=value)
                elif key == 'score':
                    obj = StudyRecord.objects.filter(pk=id[0]).update(score=value)
            return redirect(request.path_info)
        sobj = StudyRecord.objects.filter(course_record=course_id)
        score_choices = StudyRecord.score_choices
        return render(request, 'score.html', locals())

    def extra_url(self):
        temp = []
        temp.append(path("change_score/<int:course_id>/", self.change_score))
        return temp

    # 修改成绩
    def update_score(self, obj=None, is_header=False):
        if is_header:
            return '修改成绩'
        return mark_safe(f'<a href="change_score/{obj.pk}/">批改</a>')

    def StudyRecordAdd(self, request, queryset):
        temp = []
        for course_obj in queryset:
            sobj = Student.objects.filter(class_list__pk=course_obj.class_obj.pk)
            for student in sobj:
                if not StudyRecord.objects.filter(course_record=course_obj,
                                                  student=student).exists():  # 判断是否存在重复数据避免重复提交
                    temp.append(StudyRecord(course_record=course_obj, student=student))
        StudyRecord.objects.bulk_create(temp)

    StudyRecordAdd.desc = '批量添加考情记录'

    def modify_record(self, obj=None, is_header=False):
        if is_header:
            return '操作学生记录'
        return mark_safe(f'<a href="/Xadmin/crm/studyrecord/?course_record={obj.pk}">查看</a>')

    list_display = ["class_obj", 'day_num', 'teacher', 'date', modify_record, update_score]
    actions = [StudyRecordAdd]


site.register(CourseRecord, CourseRecordConfig)


class StudyRecordConfig(ModelAdmin):
    list_display = ["student", 'course_record', 'record', 'score']


site.register(StudyRecord, StudyRecordConfig)
site.register(FuthurDetail)

