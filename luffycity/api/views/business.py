import datetime
import json
from django.contrib.contenttypes.models import ContentType
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet, ViewSetMixin
from api.serializers import CourseSerializer, CourseDetailSerializer, ArticleSerializer, ArticleDetailSerializer
from django_redis import get_redis_connection
from api.models import Course, CourseDetail, Article, PricePolicy, Coupon, CouponRecord
from api.utils.MyException import ModifyPolicyException

# Create your views here.
class CourseView(ModelViewSet):
    # versioning_class = URLPathVersioning
    # queryset = Course.objects
    # serializer_class = CourseSerializer

    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': ''}
        try:
            queryset = Course.objects.all()
            serializer = CourseSerializer(queryset, many=True)
            ret['data'] = serializer.data
        except Exception as e:
            ret = {'code': 1001, 'data': '数据不正确'}
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': {}}
        try:
            queryset = CourseDetail.objects.all().filter(course_id=kwargs['pk']).first()
            data = CourseDetailSerializer(queryset, many=False)
            ret['data'] = data.data
        except Exception as e:
            print(e)
            ret = {'code': 1001, 'data': '数据不正确'}
        return Response(ret)

class ArticleView(ModelViewSet):
    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': ''}
        try:
            queryset = Article.objects.all()
            serializer = ArticleSerializer(queryset, many=True)
            ret['data'] = serializer.data
        except Exception as e:
            ret = {'code': 1001, 'data': '数据不正确'}
        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': {}}
        try:
            queryset = Article.objects.all().filter(pk=kwargs['pk']).first()
            data = ArticleDetailSerializer(queryset, many=False)
            ret['data'] = data.data
        except Exception as e:
            print(e)
            ret = {'code': 1001, 'data': '数据不正确'}
        return Response(ret)

class MyResponse():
    def __init__(self, _list=False):
        self._list = _list
        self.ret = {
        }

    def set_msg(self, data='', code='', error='', no_threshold=''):
        self.ret['data'] = data
        if self._list:
            self.ret['no_threshold'] = no_threshold
        self.ret['code'] = code
        self.ret['error'] = error

        return self.ret

class Shopping(ViewSetMixin, APIView):
    conn = get_redis_connection('default')

    def list(self, request, *args, **kwargs):
        ret = MyResponse()
        shopping_list = []
        for i in self.conn.scan_iter(f"shopping_car_{request.user.id}_*"):
            shopping_list.append({
                'id': self.conn.hget(i, 'id').decode('utf-8'),
                'title': self.conn.hget(i, 'title').decode('utf-8'),
                'img': self.conn.hget(i, 'img').decode('utf-8'),
                'default_policy': self.conn.hget(i, 'default_policy').decode('utf-8'),
                'policy': json.loads(self.conn.hget(i, 'policy').decode('utf-8')),
            })
        return Response(ret.set_msg(data=shopping_list, code=1002))

    def create(self, request, *args, **kwargs):
        course_id = request.data.get('course_id')
        price_id = request.data.get('price_id')
        ret = MyResponse()
        try:
            model_id = ContentType.objects.get_for_model(Course).id
            price_obj = PricePolicy.objects.get(content_type_id=model_id, object_id=course_id, id=price_id)
            date = {
                "id": course_id,
                "title": price_obj.content_object.name,
                "img": price_obj.content_object.course_img,
                "default_policy": price_obj.id,
                "policy": json.dumps(
                    {p.id: {'period': p.valid_period, "valid_period": p.get_valid_period_display(), "price": p.price}
                     for p in
                     price_obj.content_object.price_policy.all()}, ensure_ascii=False)

            }
            self.conn.hmset(f"shopping_car_{request.user.id}_{course_id}", date)
            return Response(ret.set_msg(data='添加成功', code=1002))
        except Exception as e:
            print(e)
            return Response(ret.set_msg(error='课程或价格策略不存在', code=1004))

    def retrieve(self, request, *args, **kwargs):
        course_id = request.data.get('course_id')
        price_id = request.data.get('price_id')
        ret = MyResponse()
        try:
            shopping_list = f"shopping_car_{request.user.id}_{course_id}"
            print(self.conn.keys(shopping_list))
            if not self.conn.exists(shopping_list):
                raise ModifyPolicyException('没有添加该课程')
            model_id = ContentType.objects.get_for_model(Course).id
            price_obj = PricePolicy.objects.get(content_type_id=model_id, object_id=course_id, id=price_id)
            self.conn.hset(shopping_list, "default_policy", price_id)
            return Response(ret.set_msg(code=1002, data='修改成功'))
        except ModifyPolicyException as e:
            return Response(ret.set_msg(code=1004, error=e.msg))
        except Exception as e:
            return Response(ret.set_msg(code=1004, error='课程或价格策略不存在'))

    def destroy(self, request, *args, **kwargs):
        course_ids = request.data.get('course_ids')
        ret = MyResponse()
        try:
            shopping_list = [f"shopping_car_{request.user.id}_{course_id}" for course_id in course_ids]
            self.conn.delete(*shopping_list)
            return Response(ret.set_msg(data='删除成功', code=1002))
        except Exception as e:
            return Response(ret.set_msg(code=1004, error='删除失败'))

class Buy(ViewSetMixin, APIView):
    model_id = ContentType.objects.get_for_model(Course).id
    conn = get_redis_connection('default')

    def list(self, request, *args, **kwargs):
        ret = MyResponse(_list=True)
        shopping_list = []
        try:
            for i in self.conn.scan_iter(f"buy_list_{request.user.id}_*"):
                shopping_list.append({self.conn.hget(i, 'id').decode('utf-8'): {
                    'title': self.conn.hget(i, 'title').decode('utf-8'),
                    'img': self.conn.hget(i, 'img').decode('utf-8'),
                    'period': self.conn.hget(i, 'period').decode('utf-8'),
                    'valid_period': self.conn.hget(i, 'valid_period').decode('utf-8'),
                    'price': self.conn.hget(i, 'price').decode('utf-8'),
                    'default_coupon': json.loads(self.conn.hget(i, 'default_coupon').decode('utf-8')),
                    'coupon': json.loads(self.conn.hget(i, 'coupon').decode('utf-8'))
                }})
            no_threshold = json.loads(
                self.conn.hget(f'no_threshold_coupon_{request.user.id}', 'no_threshold').decode('utf-8'))
            no_threshold.update({'default_coupon': self.conn.hget(f'no_threshold_coupon_{request.user.id}',
                                                                  'default_coupon').decode('utf-8')})
            return Response(ret.set_msg(data=shopping_list, no_threshold=no_threshold, code=1002))
        except Exception as e:
            print(e)
            return Response(ret.set_msg(error='获取结算清单异常', code=1002))

    def create(self, request, *args, **kwargs):
        course_ids = request.data.get('course_ids')
        ret = MyResponse()
        try:
            if len(course_ids) == 0:
                raise ModifyPolicyException('未添加任何课程')
            # 查询当前用户所有的优惠券
            coupon_list = CouponRecord.objects.filter(
                account__pk=request.user.id, status=0,
                coupon__valid_end_date__gte=datetime.date.today(),
                coupon__valid_begin_date__lte=datetime.date.today())
            for id in course_ids:
                course_id = f"shopping_car_{request.user.id}_{id}"
                if self.conn.exists(course_id):
                    data = {}
                    data['id'] = id
                    data["title"] = self.conn.hget(course_id, 'title').decode('utf-8')
                    data["img"] = self.conn.hget(course_id, 'img').decode('utf-8')
                    data.update(json.loads(self.conn.hget(course_id, 'policy').decode('utf-8'))[
                                    str(self.conn.hget(course_id, 'default_policy').decode('utf-8'))])
                    # 筛选课程下的优惠券
                    data["coupon"] = json.dumps(
                        [{c.coupon.id: {'name': c.coupon.name, 'coin': c.coupon.money_equivalent_value,
                                        'minimum': c.coupon.minimum_consume, 'discount': c.coupon.off_percent,
                                        'type': c.coupon.coupon_type}}
                         for c in
                         coupon_list if c.coupon.object_id == id],
                        ensure_ascii=False)
                    data["default_coupon"] = 0
                    self.conn.hmset(f'buy_list_{request.user.id}_{id}', data)
            # 筛选全局优惠券
            self.conn.hmset(f'no_threshold_coupon_{request.user.id}', {"no_threshold": json.dumps({"coupon":
                [{
                    c.coupon.id: {
                        'name': c.coupon.name,
                        'coin': c.coupon.money_equivalent_value,
                        'minimum': c.coupon.minimum_consume,
                        'discount': c.coupon.off_percent,
                        'type': c.coupon.coupon_type}}
                    for c in
                    coupon_list if
                    not c.coupon.content_object]},
                ensure_ascii=False),
                'default_coupon': 0})
            return Response(ret.set_msg(code=1002, data='添加成功'))
        except ModifyPolicyException as e:
            return Response(ret.set_msg(code=1004, error=e.msg))
        except Exception as e:
            print(e)
            return Response(ret.set_msg(error='课程或价格策略不存在', code=1004))

    def retrieve(self, request, *args, **kwargs):
        course_id = request.data.get('course_id')
        coupon_id = request.data.get('coupon_id')
        ret = MyResponse()
        try:
            if coupon_id == 0:
                coupon_type = request.data.get('coupon_type')
                if coupon_type == 'all':
                    self.conn.hset(f'no_threshold_coupon_{request.user.id}', 'default_coupon', coupon_id)
                elif coupon_type == 'part':
                    buying_list = f"buy_list_{request.user.id}_{course_id}"
                    if not self.conn.exists(buying_list):
                        raise ModifyPolicyException('没有添加该商品')
                    self.conn.hset(buying_list, 'default_coupon', coupon_id)
            else:
                couponrecord_obj = CouponRecord.objects.get(coupon_id=coupon_id, account_id=request.user.id)
                if couponrecord_obj.coupon.content_object == None:
                    self.conn.hset(f'no_threshold_coupon_{request.user.id}', 'default_coupon', coupon_id)
                else:
                    buying_list = f"buy_list_{request.user.id}_{course_id}"
                    if not self.conn.exists(buying_list):
                        raise ModifyPolicyException('没有添加该商品')
                    model_id = ContentType.objects.get_for_model(Course).id
                    price_obj = Coupon.objects.get(content_type_id=model_id, object_id=course_id, id=coupon_id)
                    self.conn.hset(buying_list, "default_coupon", coupon_id)
            return Response(ret.set_msg(code=1002, data='修改成功'))
        except ModifyPolicyException as e:
            return Response(ret.set_msg(code=1004, error=e.msg))
        except Exception as e:
            print(e)
            return Response(ret.set_msg(code=1004, error='优惠券不存在'))

    # def destroy(self, request, *args, **kwargs):
    #     course_ids = request.data.get('course_ids')
    #     ret = MyResponse()
    #     try:
    #         shopping_list = [f"shopping_car_{request.user.id}_{course_id}" for course_id in course_ids]
    #         self.conn.delete(*shopping_list)
    #         return Response(ret.set_msg(data='删除成功', code=1002))
    #     except Exception as e:
    #         return Response(ret.set_msg(code=1004, error='删除失败'))
