from django.test import TestCase
from lists.views import home_page
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

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
        response=self.client.post('/',data={'item_text':'A new list item'})
        self.assertIn('A new list item',response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
