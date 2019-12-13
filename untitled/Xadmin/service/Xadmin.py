from django.urls import path
from django.shortcuts import HttpResponse, render, redirect
from django.utils.safestring import mark_safe
from django.shortcuts import reverse
from Xadmin.utils.mypage import Pagination
from django.db.models import Q
from django.db.models.fields.related import ManyToManyField, ForeignKey, ManyToManyRel
from django.forms import ChoiceField,MultipleChoiceField,ModelChoiceField


class ShowList():
    def __init__(self, obj, data_list, request):
        page_num = request.GET.get('page', 1)
        self.request = request
        self.obj = obj
        self.data_list = data_list
        self.page = Pagination(page_num, data_list.count(), obj.get_list_url(), request.GET, per_page=10, max_page=11)
        self.page_list = self.data_list[self.page.start:self.page.end]
        self.action = self.obj.actions
        # self.action.insert(0, getattr(self.obj, 'default'))

    def get_list_url(self):
        temp = {}
        for field in self.obj.list_filter:
            # 复制get请求方法的所有数据
            params = self.request.GET.copy()
            cid = self.request.GET.get(field, 0)
            # 获取模型字段属性
            field_obj = self.obj.model._meta.get_field(field)
            # 通过模型字段属性获取关联对象模块的所有值
            if isinstance(field_obj, ManyToManyField) or isinstance(field_obj, ForeignKey) or isinstance(field_obj,
                                                                                                         ManyToManyRel):
                data_list = field_obj.remote_field.model.objects.all()
            else:
                data_list = self.obj.model.objects.all().values('pk', field)
            links_list = []
            if params.get(field):
                del params[field]
            links_list.append(f'<a {"class=active" if cid == 0 else ""} href="?{params.urlencode()}">All</a>')
            for data in data_list:
                # 判断数据类型是否满足关系
                if isinstance(field_obj, ManyToManyField) or isinstance(field_obj, ForeignKey) or isinstance(field_obj,
                                                                                                             ManyToManyRel):
                    params[field] = data.pk
                    pk = data.pk
                    text = str(data)
                else:
                    pk = data.get('pk')
                    text = data.get(field)
                    params[field] = text
                if cid == str(pk) or cid == text:
                    _url = f'<a class="active" href="?{params.urlencode()}">{text}</a>'
                else:
                    _url = f'<a href="?{params.urlencode()}">{text}</a>'
                links_list.append(_url)
            temp[field] = links_list
        return temp

    def get_action_list(self):
        temp = []
        temp.append({'name': getattr(self.obj, 'default').__name__, 'desc': getattr(self.obj, 'default').__name__})
        for i in self.action:
            temp.append({'name': i.__name__, 'desc': i.desc if i.desc else i.__name__})
        return temp

    def get_head(self):
        head_list = []
        if not self.obj.head_list:
            for name in self.obj.new_list_display():
                if isinstance(name, str):
                    # 如果是 __str__ 返回当前对象
                    if name == '__str__':
                        val = self.obj.model._meta.model_name
                    else:
                        # 获取字段对象的verbose_name self.model._meta.get_field(name).verbose_name
                        val = self.obj.model._meta.get_field(name).verbose_name
                else:
                    val = name(self.obj, is_header=True)
                head_list.append(val)
        else:
            if len(self.obj.new_head_display()) > len(self.obj.new_list_display()):
                raise Exception('展示头和数据量不一致')
            head_list = self.obj.new_head_display()
        return head_list

    def get_body(self):
        new_data_list = []
        for data in self.page_list:
            temp = []
            for filter in self.obj.new_list_display():
                if isinstance(filter, str):
                    if filter == '__str__':
                        val = getattr(data, filter)
                    else:
                        field_obj = self.obj.model._meta.get_field(filter)
                        # 判断是否为多对多字段
                        if isinstance(field_obj, ManyToManyField):
                            # 符合就生成字符串数据
                            val = ','.join([str(i) for i in getattr(data, filter).all()])
                        else:
                            # 对设置了choices属性 直接获取key对应的描述数据
                            if field_obj.choices:
                                val = getattr(data, f'get_{filter}_display')
                            else:
                                val = getattr(data, filter)
                    if filter in self.obj.list_display_links:
                        val = mark_safe(f'<a href="{self.obj.get_change_url(data)}">{val}</a>')
                else:
                    val = filter(self.obj, data)
                temp.append(val)
            new_data_list.append(temp)

        return new_data_list


class ModelAdmin():
    list_display = ['__str__']
    list_display_links = []
    head_list = []
    moderlform_class = None
    search_field = []
    actions = []
    list_filter = []

    def default(self, request, queryset):
        queryset.delete()

    def __init__(self, model, site):
        self.model = model
        self.site = site

    def get_model_form(self):
        if not self.moderlform_class:
            from django.forms import ModelForm
            class ModerlFormClass(ModelForm):
                class Meta:
                    model = self.model
                    fields = '__all__'

            self.moderlform_class = ModerlFormClass
        return self.moderlform_class

    def get_change_url(self, obj):
        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label
        _url = reverse("%s_%s_change" % (app_label, model_name), args=(obj.pk,))
        return _url

    def get_delete_url(self, obj):
        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label
        _url = reverse("%s_%s_delete" % (app_label, model_name), args=(obj.pk,))
        return _url

    def get_add_url(self):
        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label
        _url = reverse("%s_%s_add" % (app_label, model_name))
        return _url

    def get_list_url(self):
        model_name = self.model._meta.model_name
        app_label = self.model._meta.app_label
        _url = reverse("%s_%s_list" % (app_label, model_name))
        return _url

    def checkbox(self, obj=None, is_header=False):
        if is_header:
            return mark_safe('<input id="choice" type="checkbox">')
        return mark_safe(f'<input class="item_choices" type="checkbox" value={obj.pk} name="select_list"')

    def edit(self, obj=None, is_header=False):
        if is_header:
            return '编辑'
        return mark_safe(f'<a href="{self.get_change_url(obj)}">编辑</a>')

    def deletes(self, obj=None, is_header=False):
        if is_header:
            return '删除'
        return mark_safe(f'<a href="{self.get_delete_url(obj)}">删除</a>')

    # 重构自定义列表 在其前面与后面添加默认列
    def new_list_display(self):
        temp = []
        temp.append(ModelAdmin.checkbox)
        temp.extend(self.list_display)
        if not self.list_display_links:
            temp.append(ModelAdmin.edit)
        temp.append(ModelAdmin.deletes)
        return temp

    def new_head_display(self):
        temp = []
        temp.append(ModelAdmin.checkbox(self, is_header=True))
        temp.extend(self.head_list)
        temp.append(ModelAdmin.edit(self, is_header=True))
        temp.append(ModelAdmin.deletes(self, is_header=True))
        return temp

    def get_search_model(self, request):
        key_word = request.GET.get('search', '')
        search_condition = Q()
        search_condition.connector = 'or'
        if self.search_field:
            for field in self.search_field:
                search_condition.children.append((field + '__contains', key_word))
        return search_condition

    def get_filter_model(self, request):
        filter_condition = Q()
        filter_condition.connector = 'and'
        for field, value in request.GET.items():
            if field in self.list_filter or field !='page':
                filter_condition.children.append((field, value))
        return filter_condition

    def list_view(self, request):
        if request.method == 'POST':
            action = request.POST.get('action')
            select_list = request.POST.getlist('select_list')
            # 选择错误时捕获异常给予正确提示
            try:
                fun_obj = getattr(self, action)
            except:
                return HttpResponse('选择错误')
            queryset = self.model.objects.filter(pk__in=select_list)
            fun_obj(request, queryset)
        new_request = request.GET.copy()
        search_condition = self.get_search_model(request)
        filter_condition = self.get_filter_model(request)
        data_list = self.model.objects.filter(search_condition).filter(filter_condition)
        showlist = ShowList(self, data_list, request)
        return render(request, 'list.html', {'showlist': showlist,
                                             'model_name': self.model._meta.model_name, 'add_url': self.get_add_url()})

    def add_view(self, request):
        ModelClass = self.get_model_form()
        form = ModelClass()
        if request.method == 'POST':
            form = ModelClass(request.POST)
            if form.is_valid():
                obj=form.save()
                pop_id=request.GET.get('pop_id')
                if pop_id:
                    return render(request,'pop.html', {'id':obj.pk,'text':str(obj),'pop_id':pop_id})
                return redirect(self.get_list_url())
        for field in form:
            # from django.forms.boundfield import BoundField
            # print(type(field))
            if isinstance(field.field, ModelChoiceField):
                field.is_pop = True
                # field.field.queryset.model 通过boundfield对象获取模型对象 field.name 获取当前字段名称
                _url =reverse(f'{field.field.queryset.model._meta.app_label}_{field.field.queryset.model._meta.model_name}_add')
                field.url=_url+f'?pop_id=id_{field.name}'
        return render(request, 'add_view.html', {'form': form})

    def change_view(self, request, id):
        model_obj = self.model.objects.filter(pk=id).first()
        ModelClass = self.get_model_form()
        if model_obj:
            form = ModelClass(instance=model_obj)  # 将数据带入到页面中
            if request.method == 'POST':
                form = ModelClass(request.POST, instance=model_obj)
                if form.is_valid():
                    obj=form.save()
                    pop_id = request.GET.get('pop_id')
                    if pop_id:
                        return render(request, 'pop.html', {'id': obj.pk, 'text': str(obj), 'pop_id': pop_id})
                    return redirect(self.get_list_url())
        else:
            return HttpResponse('Not exist')
        for field in form:
            if isinstance(field.field, ModelChoiceField):
                field.is_pop = True
                _url = reverse(f'{field.field.queryset.model._meta.app_label}_{field.field.queryset.model._meta.model_name}_add')
                field.url = _url + f'?pop_id=id_{field.name}'
        return render(request, 'change_view.html', {'form': form})

    def delete_view(self, request, id):
        model_obj = self.model.objects.filter(pk=id)
        if model_obj:
            if request.method == 'POST':
                model_obj.delete()
                return redirect(self.get_list_url())
        else:
            return HttpResponse('不存在')
        return render(request, 'delete_view.html', {'url': self.get_list_url()})

    @property
    def get_urls(self):
        app_name = self.model._meta.app_label
        model_name = self.model._meta.model_name
        temp = [
            path('', self.list_view, name=f'{app_name}_{model_name}_list'),
            path('add/', self.add_view, name=f'{app_name}_{model_name}_add'),
            path('<int:id>/change/', self.change_view, name=f'{app_name}_{model_name}_change'),
            path('<int:id>/delete/', self.delete_view, name=f'{app_name}_{model_name}_delete')
        ]
        if hasattr(self,'extra_url'):
            temp.extend(self.extra_url())
        return temp, None, None


class XadminSite():
    def __init__(self, name='admin'):
        self._registry = {}  # model_class class -> admin_class instance
        self.name = name

    def register(self, model, admin_class=None):
        if not admin_class:
            Xadmin_class = ModelAdmin
        else:
            Xadmin_class = admin_class
        self._registry[model] = Xadmin_class(model, self)

    @property
    def urls(self):
        temp = []
        for model, Xadmin_class in self._registry.items():
            app_name = model._meta.app_label
            model_name = model._meta.model_name
            # 路由分发
            temp.append(path(f'{app_name}/{model_name}/', Xadmin_class.get_urls))
        return temp, None, None


site = XadminSite()
