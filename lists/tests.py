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
        expected_html = render_to_string('home.html')
        self.assertEqual(expected_html, html)

    # 校验当前模板
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
