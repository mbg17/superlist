from django.test import TestCase
from lists.views import home_page
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item, List

# Create your tests here.


# class HomePageTest(TestCase)
class NewListTest(TestCase):
    # 测试url能否解析
    # def test_root_url_resolves_to_home_page_view(self):
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)

    # 测试页面是否正确
    # def test_home_page_reyurns_correct_html(self):
    #     #request = HttpRequest()
    #     response = self.client.get('/')
    #     html = response.content.decode('utf-8')
    #     # 初始对比网页返回值
    #     # self.assertTrue(html.startswith('<html>'))
    #     # self.assertIn('<title>To-Do lists</title>',html)
    #     # self.assertTrue(html.endswith('</html>'))
    #     # 手动渲染模板
    #     try:
    #         expected_html = render_to_string('home.html')
    #         self.assertEqual(expected_html, html)
    #     except Exception:
    #         pass

    # 校验当前模板
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    # 测试能否成功响应POST请求
    def test_can_save_a_POST_request(self):
        #向目标地址传送数据 data={标签name:值}
        response = self.client.post(
            '/lists/new', data={'item_text': 'A new list item'})

        # 测试数据库写入
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    # 测试是否重定向
    def test_redirects_after_POST(self):
        response = self.client.post(
            '/lists/new', data={'item_text': 'A new list item'})
        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response["location"],
        #                  '/lists/the-only-list-in-the-world/')
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')

    # 测试成功保存一个数据后的结果
    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    # 测试数据是否存入数据库
    # def test_displays_all_list_items(self):
    #     Item.objects.create(text='itemey 1')
    #     Item.objects.create(text='itemey 2')
    #     reponse=self.client.get('/')
    #     self.assertIn('itemey 1',reponse.content.decode())
    #     self.assertIn('itemey 2',reponse.content.decode())


    # 数据模型测试
class ListAndItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        # 存储数据
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        # 获取所有数据对象
        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        list_ = List.objects.create()
        # f 局部变量
        response = self.client.get(f'/lists/{list_.id}/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_that_list(self):
        # 创建外键
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text='other list item 1', list=other_list)
        Item.objects.create(text='other list item 2', list=other_list)
        response = self.client.get(f'/lists/{correct_list.id}/')
        # assertContains 处理响应请求 (同 response.content.decode() (decode() bytes类型转str类型))
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2')


class NewItemTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        self.client.post(f'/lists/{correct_list.id}/add_item',\
        data={'item_text': 'A new item for an existing list'})
        self.assertEqual(Item.objects.count(),1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text,'A new item for an existing list')
        self.assertEqual(new_item.list,correct_list)

    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response=self.client.post(f'/lists/{correct_list.id}/add_item',\
        data={'item_text': 'A new item for an existing list'})

        self.assertRedirects(response,f'/lists/{correct_list.id}/')
    
    def test_passer_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response=self.client.get(f'/lists/{correct_list.id}/')
        self.assertEqual(response.context['list'],correct_list)