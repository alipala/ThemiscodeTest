import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Pages.LoginPage import LoginPage
from Base.base import Base
import allure
import pytest
import pandas as pd


@pytest.mark.usefixtures('set_up')
class TestLogin(Base):

    __user_data_file = r"\login_details.xlsx"
    df = pd.read_excel(os.getcwd() + __user_data_file)

    @allure.feature("Login Success")
    @allure.story("The user should login by typing credentials")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_success(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email(self.df.loc[0,"username"])
        login.enter_password(self.df.loc[0,"pass"])
        login.click_login()

        # Allure screenshot for the test
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)

        try:
            assert "Ana Sayfa - Dava & İcra" == driver.title
        except Exception as e:
            raise
            print("Title is wrong", format(e))

    @allure.feature("Login Fail")
    @allure.story("The user should not be entered with wrong credentials")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_fail(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email(self.df.loc[1,"username"])
        login.enter_password(self.df.loc[1,"pass"])
        login.click_login()
        try:
            assert "Giriş - Dava & İcra Takip" == driver.title
            print("Title is ok")
        except Exception as e:
            raise
            print("Title is wrong", format(e))

