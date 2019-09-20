import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Base.base import Base
import pandas as pd
import allure
import pytest


@allure.feature("Ana sayfa logout")
class TestHome(Base):
    __user_data_file = r"\login_details.xlsx"
    df = pd.read_excel(os.getcwd() + __user_data_file)

    @allure.story('Logout')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase('TESTCASE-1')
    def test_home_logout(self):
        driver = self.driver
        self.login()
        home = HomePage(driver)
        home.logout()
        try:
            # Allure screenshot for the test
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
            assert "Giriş - Dava & İcra Takip" in driver.title
            print("Title is ok")
        except Exception as e:
            print("Title is wrong", format(e))


    # Helper function
    def login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email(self.df.loc[0,"username"])
        login.enter_password(self.df.loc[0,"pass"])
        login.click_login()
