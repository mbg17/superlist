from selenium import webdriver
import unittest

class NewVistorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")
        # 断言 assertIn assertEqual assertTrue assertFalse
        self.assertIn('To-do',self.browser.title)

        self.fail("Finish the test")


if __name__=='__main__':
    unittest.main(warnings='ignore')


