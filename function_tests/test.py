from selenium import webdriver
# import unittest
from django.test import LiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


class NewVistorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

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
        # time.sleep(1)

        # 对比列表是否包含数据
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        # self.assertIn('1:Buy peacock feathers', [row.text for row in rows])
        # self.assertIn('Buy peacock feathers to make a fly',
        #               [row.text for row in rows])
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
        
        edith_list_url=self.browser.current_url
        # 正则匹配当前url
        self.assertRegex(edith_list_url,'/list/.+')

        self.browser.quit()

        self.browser=webdriver.Firefox()
        self.browser.get(self.live_server_url)
        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_now_in_list_table('1:Buy milk')

        francis_list_url=self.browser.current_url
        self.assertRegex(francis_list_url,'/list/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)

        page_text=self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertIn('Buy milk',page_text)






