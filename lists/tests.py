from django.test import TestCase
from lists.views import home_page
from django.urls import resolve
from django.http import HttpRequest
# Create your tests here.

class HomePageTest(TestCase):
    # 测试url能否解析
    def test_root_url_resolves_to_home_page_view(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)
    # 测试页面是否正确
    def test_home_page_reyurns_correct_html(self):
        request=HttpRequest()
        response=home_page(request)
        html =response.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.endswith('</html>'))
