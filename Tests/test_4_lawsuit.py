import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Pages.LawsuitPage import LawsuitPage
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Base.base import Base
import pandas as pd
import allure
import pytest


@allure.feature('Dava Dosyaları tabı altındaki işlemler')
class TestLawsuit(Base):
    __user_data_file = r"\login_details.xlsx"
    df = pd.read_excel(os.getcwd() + __user_data_file)

    # @allure.story('Sayfa başlığı kontrol')
    # @allure.severity(allure.severity_level.NORMAL)
    # @allure.testcase('TESTCASE-1')
    # def test_law_suit_page_title(self):
    #     driver = self.driver
    #     self.login()
    #     home = HomePage(driver)
    #     home.click_law_suit_page()
    #     try:
    #         # Allure screenshot for the test
    #         allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
    #         assert "Dava Dosyaları - Dava & İcra Takip" in driver.title
    #         print("Title is ok")
    #     except Exception as e:
    #         raise
    #         print("Title is wrong", format(e))
    #
    # @allure.story('Davaları Listele')
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.testcase('TESTCASE-2')
    # def test_case_list_records(self):
    #     driver = self.driver
    #     self.login()
    #     lawsuit = LawsuitPage(driver)
    #     home = HomePage(driver)
    #     home.click_law_suit_page()
    #     lawsuit.case_list_records()

    @allure.story('Dava yarat ve kaydet')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('TESTCASE-3')
    def test_case_create_save(self):
        driver = self.driver
        lawsuit = LawsuitPage(driver)
        self.login()
        self.case_create()
        lawsuit.save_case()

    # @allure.story('Dava yarat ve kaydetme')
    # @allure.severity(allure.severity_level.NORMAL)
    # @allure.testcase('TESTCASE-4')
    # def test_case_create_discard(self):
    #     driver = self.driver
    #     lawsuit = LawsuitPage(driver)
    #     self.login()
    #     self.case_create()
    #     lawsuit.discard_case()

    # @allure.story('Dava düzenle')
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.testcase('TESTCASE-5')
    # def test_edit_last_case(self):
    #     driver = self.driver
    #     self.login()
    #     lawsuit = LawsuitPage(driver)
    #     home = HomePage(driver)
    #     home.click_law_suit_page()
    #     lawsuit.case_entry_information_edit()

    # @allure.story('Dava numarasına göre filtrele')
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.testcase('TESTCASE-6')
    # def test_find_case_file_by_no(self):
    #     driver = self.driver
    #     self.login()
    #     home = HomePage(driver)
    #     home.click_law_suit_page()
    #     lawsuit = LawsuitPage(driver)
    #     lawsuit.filter_case_by_file_no()

    # @allure.story('Dava durumuna göre filtrele')
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.testcase('TESTCASE-7')
    # def test_find_case_file_by_case_state(self):
    #     driver = self.driver
    #     self.login()
    #     home = HomePage(driver)
    #     home.click_law_suit_page()
    #     lawsuit = LawsuitPage(driver)
    #     lawsuit.filter_case_by_case_state()
    #
    # @allure.story('Dava tipine göre filtrele')
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.testcase('TESTCASE-8')
    # def test_find_case_file_by_case_type(self):
    #     driver = self.driver
    #     self.login()
    #     home = HomePage(driver)
    #     home.click_law_suit_page()
    #     lawsuit = LawsuitPage(driver)
    #     lawsuit.filter_case_by_case_type()
    #
    # @allure.story('Dosya no filtresi temizle')
    # @allure.severity(allure.severity_level.MINOR)
    # @allure.testcase('TESTCASE-9')
    # def test_clear_sheet_no_filter(self):
    #     driver = self.driver
    #     self.login()
    #     home = HomePage(driver)
    #     home.click_law_suit_page()
    #     lawsuit = LawsuitPage(driver)
    #     lawsuit.filter_case_by_file_no()
    #     lawsuit.clear_filtered_search()
    #
    # @allure.story('Bir önceki sayfaya dön')
    # @allure.severity(allure.severity_level.CRITICAL)
    # @allure.testcase('TESTCASE-10')
    # def test_back_previous_page(self):
    #     driver = self.driver
    #     self.login()
    #     home = HomePage(driver)
    #     home.click_law_suit_page()
    #     lawsuit = LawsuitPage(driver)
    #     lawsuit.filter_case_by_file_no()
    #     lawsuit.back_previous_page()

    # Helper functions
    def login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email(self.df.loc[0,"username"])
        login.enter_password(self.df.loc[0,"pass"])
        login.click_login()

    def case_create(self):
        driver = self.driver
        home = HomePage(driver)
        home.click_law_suit_page()
        lawsuit = LawsuitPage(driver)
        lawsuit.click_case_create_btn()
        lawsuit.fill_case_information()
        lawsuit.fill_client_information()
        lawsuit.fill_defendant_information()
        lawsuit.fill_details()