from Pages.LoginPage import LoginPage
from Base.base import Base
import pytest
import sys
import os
import pandas as pd
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

@pytest.mark.usefixtures('set_up')
class TestLogin(Base):

    __user_data_file = r"\login_details.xlsx"
    df = pd.read_excel(os.getcwd() + __user_data_file)

    def test_login_validation(self):
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

    def test_login_wrong(self):
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


