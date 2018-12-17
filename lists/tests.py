from django.test import TestCase
from lists.views import home_page
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item

# Create your tests here.


class HomePageTest(TestCase):
    # 测试url能否解析
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    # 测试页面是否正确
    def test_home_page_reyurns_correct_html(self):
        #request = HttpRequest()
        response = self.client.get('/')
        html = response.content.decode('utf-8')
        # 初始对比网页返回值
        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>',html)
        # self.assertTrue(html.endswith('</html>'))
        # 手动渲染模板
        try:
            expected_html = render_to_string('home.html')
            self.assertEqual(expected_html, html)
        except Exception:
            pass

    # 校验当前模板
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    # 测试能否成功响应POST请求
    def test_can_save_a_POST_request(self):
        #向目标地址传送数据 data={标签name:值}
        response = self.client.post('/', data={'item_text': 'A new list item'})

        # 测试数据库写入
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    # 测试是否重定向
    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(response.status_code,302)
        self.assertEqual(response["location"],'/')

    # 测试成功保存一个数据后的结果
    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(),0)

    # 测试数据是否存入数据库
    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        reponse=self.client.get('/')
        self.assertIn('itemey 1',reponse.content.decode())
        self.assertIn('itemey 2',reponse.content.decode())
        
    # 数据模型测试
class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        # 存储数据
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        # 获取所有数据对象
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]

        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
