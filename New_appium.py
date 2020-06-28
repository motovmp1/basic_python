import time
import unittest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import HtmlTestRunner


class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        # This is the Application and ‘app’ desired capability to specify a path to Appium.
        # self.dc['app'] = "C://eribank.apk"
        # appPackage and appActivity  desired capability specify app details to Appium
        self.dc['appPackage'] = "com.experitest.ExperiBank"
        self.dc['appActivity'] = ".LoginActivity"
        # platformName desired capability specify platform detail to Appium
        self.dc['platformName'] = 'Android'
        # deviceName desired capability specify the device id detail to Appium
        # device id is got from running adb devices command in PC
        self.dc['deviceName'] = '7ebb211'
        # Creating the Driver by passing Desired Capabilities.
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)

    def test_Login_na_conta(self):
        if len(self.driver.find_elements_by_xpath("//*[@text='OK']")) > 0:
            self.driver.find_element_by_xpath("//*[@text='OK']").click()
        # Find location of Elements and perform action.
        self.driver.find_element_by_xpath("//*[@text='Username']").send_keys('company')
        self.driver.find_element_by_xpath("//*[@text='Password']").send_keys('company')
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@text='Login']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@text='Logout']").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))
