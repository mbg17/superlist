from selenium import webdriver
# import unittest
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
import time


class NewVistorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    # 对比数据
    def check_for_now_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # self.live_server_url获取本地地址
        self.browser.get(self.live_server_url)
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
        time.sleep(1)

        # 对比列表是否包含数据
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        # self.assertIn('1:Buy peacock feathers', [row.text for row in rows])
        # self.assertIn('Buy peacock feathers to make a fly',
        #               [row.text for row in rows])
        self.check_for_now_in_list_table('1:Buy peacock feathers')
        self.check_for_now_in_list_table('2:Buy peacock feathers to make a fly')
        #完成测试
        self.fail("Finish the test")



