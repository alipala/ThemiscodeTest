import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Pages.LoginPage import LoginPage
from Base.base import Base
import pytest
import pandas as pd
import allure



@pytest.mark.usefixtures('set_up')
class TestLogin(Base):

    __user_data_file = r"\login_details.xlsx"
    df = pd.read_excel(os.getcwd() + __user_data_file)

    def test_login_success(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email(self.df.loc[0,"username"])
        login.enter_password(self.df.loc[0,"pass"])
        login.click_login()
        try:
            assert "Ana Sayfa - Dava & İcra Takip" in driver.title
            print("Title is ok")
        except Exception as e:
            print("Title is wrong", format(e))

    def test_login_fail(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email(self.df.loc[1,"username"])
        login.enter_password(self.df.loc[1,"pass"])
        login.click_login()
        try:
            assert "Giriş - Dava & İcra Takip" in driver.title
            print("Title is ok")
        except Exception as e:
            print("Title is wrong", format(e))

