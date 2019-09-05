import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Base.base import Base
import pandas as pd
import allure
import pytest
import time


class TestHomeWelcome(Base):
    __user_data_file = r"\login_details.xlsx"
    df = pd.read_excel(os.getcwd() + __user_data_file)

    # @allure.feature("Home page welcome user click")
    # @allure.story("The user may click the welcome user link")
    # @allure.severity(allure.severity_level.NORMAL)
    def test_home_welcome_link(self):
        driver = self.driver
        self.login()
        home = HomePage(driver)
        home.click_welcome_user_link()
        try:
            assert "The user name is " == driver.title
        except Exception as e:
            raise
            print("The welcome link does not work", format(e))

    # Helper function
    def login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email(self.df.loc[0, "username"])
        login.enter_password(self.df.loc[0, "pass"])
        login.click_login()
