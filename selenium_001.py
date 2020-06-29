from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get("https://google.com")
        self.url_under_test = self.driver.current_url
        print(self.url_under_test)
        assert self.url_under_test == "https://www.google.com/"
        self.driver.find_element_by_name("q").send_keys("UOL")
        time.sleep(3)
        self.driver.find_element_by_name("q").send_keys(Keys.ESCAPE)
        time.sleep(3)
        self.driver.find_element_by_id("gsr").click()

    def test_search_vinicius(self):
        self.driver.get("https://google.com")
        self.url_under_test = self.driver.current_url
        print(self.url_under_test)
        assert self.url_under_test == "https://www.google.com/"
        self.driver.find_element_by_name("q").send_keys("vinicius")
        time.sleep(3)
        self.driver.find_element_by_name("q").send_keys(Keys.ESCAPE)
        time.sleep(3)
        self.driver.find_element_by_id("gsr").click()

    @classmethod
    def tearDownClass(cls):
        # close navigator
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="report_selenium"))
