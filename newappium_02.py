import time
import unittest
from appium import webdriver
import HtmlTestRunner
from locators import *
from selenium.common.exceptions import NoSuchElementException


class AppiumTest(unittest.TestCase):
    dc = {}
    driver = None

    def setUp(self):
        # This is the Application and ‘app’ desired capability to specify a path to Appium.
        # appPackage and appActivity  desired capability specify app details to Appium
        self.dc['appPackage'] = app_package_used
        self.dc['appActivity'] = appActivity_used
        # platformName desired capability specify platform detail to Appium
        self.dc['platformName'] = os_mobile
        # This is not clear the app when insert user
        # self.dc['noReset'] = 'true'
        # deviceName desired capability specify the device id detail to Appium
        # device id is got from running adb devices command in PC
        self.dc['deviceName'] = id_mobile
        # Creating the Driver by passing Desired Capabilities.
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.dc)
        self.driver.implicitly_wait(5)

    def test_Login_na_conta(self):
        # timer para subir o banner
        time.sleep(2)
        self.driver.find_element_by_id("com.lbe.security.miui:id/permission_allow_button_1").click()
        self.driver.find_element_by_xpath("//*[@class='android.widget.ImageButton']").click()
        self.driver.find_element_by_xpath("//*[@text='Cadastrar Novo']").click()
        self.driver.find_element_by_id("br.com.dudstecnologia.cadastrodeclientes:id/editNome").send_keys(name_user1)
        self.driver.find_element_by_xpath("//*[@text='SALVAR']").click()
        self.driver.find_element_by_xpath("//*[@text='OK']").click()
        self.driver.back()

    def tearDown(self):
        time.sleep(10)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='report_cadastro'))
