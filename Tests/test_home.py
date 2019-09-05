import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Base.base import Base
import pandas as pd
import allure
import pytest


class TestHome(Base):
    __user_data_file = r"\login_details.xlsx"
    df = pd.read_excel(os.getcwd() + __user_data_file)

    # @allure.feature("Home page logout")
    # @allure.story("The user should logout from system with logout button")
    # @allure.severity(allure.severity_level.CRITICAL)
    def test_home_logout(self):
        driver = self.driver
        self.login()
        home = HomePage(driver)
        home.logout()
        try:
            assert "Ana Sayfa - Dava & İcra Takip" in driver.title
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
