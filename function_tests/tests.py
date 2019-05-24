from selenium import webdriver
# import unittest
# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
import os

# class NewVistorTest(LiveServerTestCase):
class NewVistorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        # 从输入框获取参数 linux地址：192.168.85.137
        staging_server=os.environ.get("STAGING_SERVER")
        if staging_server:
            self.live_server_url='http://'+staging_server


    def tearDown(self):
        self.browser.quit()

    # 对比数据
    def wait_for_now_in_list_table(self, row_text):
        MAX_TIME = 10
        starttime = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - starttime > MAX_TIME:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):
        # self.live_server_url获取本地地址
        self.browser.get(self.live_server_url)
        print(self.live_server_url)
        # 断言 assertIn assertEqual assertTrue assertFalse
        self.assertIn('To-Do', self.browser.title)

        # 比对h1标签是否包含有关数据
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 查找输入框 对比默认值
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # 输入数据提交
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # 对比列表是否包含数据
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # f插入局部变量
        self.assertTrue(
            any(row.text == '1:Buy peacock feathers' for row in rows),
            f"New to-do item did not apper in table. Content were:\n{table.text}"  #自定义异常输出
        )
        # 输入数据提交
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(1)

        # 对比列表是否包含数据
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        # self.assertIn('1:Buy peacock feathers', [row.text for row in rows])
        # self.assertIn('Buy peacock feathers to make a fly',
        #               [row.text for row in rows])
        # time.sleep(10)
        self.wait_for_now_in_list_table('2:Buy peacock feathers to make a fly')
        self.wait_for_now_in_list_table('1:Buy peacock feathers')
        #完成测试
        # self.fail("Finish the test")

    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_now_in_list_table('1:Buy peacock feathers')

        edith_list_url = self.browser.current_url
        # 正则匹配当前url
        self.assertRegex(edith_list_url, '/lists/.+')

        self.browser.quit()

        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_now_in_list_table('1:Buy milk')

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

    # 测试css样式
    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        # 设置窗口大小
        self.browser.set_window_size(1024, 768)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            # 获取元素位置和尺寸
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10)
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.wait_for_now_in_list_table('1:testing')
        self.assertAlmostEqual(
            # 获取元素位置和尺寸
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=10)
