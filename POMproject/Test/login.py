from selenium import webdriver
import time
import unittest
from POMproject.Pages.LoginPage import loginpage
from POMproject.Pages.Homeepage import HomePage
#import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r"C:\DriverChrome\chromedriver")
        cls.driver .implicitly_wait(10)
        cls.driver .maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = loginpage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
   # unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output = '/home/carlos/PycharmProjects/SeleniumProject/POMproject/Reports'))
   unittest.main()








