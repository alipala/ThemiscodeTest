import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Pages.CaseDetailsPage import CaseDetails
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Base.base import Base
import pandas as pd
import time
import allure


@allure.feature('Bir davanın içindeki tüm alanlar')
class TestCaseDetails(Base):
    __user_data_file = r"\login_details.xlsx"
    df = pd.read_excel(os.getcwd() + __user_data_file)

    @allure.story('Masraflar tabına git')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('TESTCASE-1')
    def test_go_expenses_tab(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.expenses_tab_entry()

    @allure.story('Alınan ödeme ekle')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase('TESTCASE-2')
    def test_add_received_payment(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.expenses_tab_entry()
        case_details.add_received_payment()

    @allure.story('Masraf ekle')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase('TESTCASE-3')
    def test_add_expense(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.expenses_tab_entry()
        case_details.add_expense()

    @allure.story('Delil olarak resim ekle')
    @allure.severity(allure.severity_level.MINOR)
    @allure.testcase('TESTCASE-4')
    def test_add_evidence_image(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.evidence_tab_entry()
        case_details.add_evidence_attachment_image()
        time.sleep(5)

    @allure.story('Delil olarak .pdf ekle')
    @allure.severity(allure.severity_level.MINOR)
    @allure.testcase('TESTCASE-5')
    def test_add_evidence_pdf(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.evidence_tab_entry()
        case_details.add_evidence_attachment_pdf()
        time.sleep(5)

    @allure.story('Delil olarak .xls ekle')
    @allure.severity(allure.severity_level.MINOR)
    @allure.testcase('TESTCASE-6')
    def test_add_evidence_excel(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.evidence_tab_entry()
        case_details.add_evidence_attachment_excel()

    @allure.story('Delilleri sil')
    @allure.severity(allure.severity_level.MINOR)
    @allure.testcase('TESTCASE-7')
    def test_delete_evidence(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.evidence_tab_entry()
        case_details.delete_evidence_attachment()

    # TODO: Need to have a look.
    # def test_load_request(self):
    #     driver = self.driver
    #     self.login()
    #     case_details = CaseDetails(driver)
    #     home = HomePage(driver)
    #     home.click_law_suit_page()
    #     case_details.request_tab_entry()
    #     case_details.load_request()

    # TODO: After implementing load_request
    # def test_delete_loaded_request(self):
    #     driver = self.driver
    #     self.login()
    #     case_details = CaseDetails(driver)
    #     home = HomePage(driver)
    #     home.click_law_suit_page()
    #     case_details.request_tab_entry()
    #     case_details.delete_loaded_request()

    @allure.story('Talimat ekle')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase('TESTCASE-8')
    def test_add_request(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.request_tab_entry()
        case_details.add_request()

    @allure.story('Talimat sil')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase('TESTCASE-9')
    def test_delete_added_request(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.request_tab_entry()
        case_details.delete_added_request()

    @allure.story('Dilekçe ekle')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase('TESTCASE-10')
    def test_add_letter_of_application(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.letter_of_application_tab_entry()
        case_details.add_letter_of_application()

    @allure.story('Dilekçe düzenle')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase('TESTCASE-11')
    def test_edit_letter_of_application(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.letter_of_application_tab_entry()
        case_details.edit_letter_of_application()

    @allure.story('Dilekçe sil')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase('TESTCASE-12')
    def test_delete_letter_of_application(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.letter_of_application_tab_entry()
        case_details.delete_letter_of_application()

    @allure.story('Tenzip zaptı ekle')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase('TESTCASE-13')
    def test_add_tenzip_zapti(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.decisions_tab_entry()
        case_details.add_tenzip_zapti()

    @allure.story('Duruşma günü ekle')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase('TESTCASE-14')
    def test_add_durusma_gunu(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.decisions_tab_entry()
        case_details.add_durusma_gunu()

    @allure.story('Kararlar/Ara Kararlar ekle')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase('TESTCASE-15')
    def test_add_kararlar(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.decisions_tab_entry()
        case_details.add_kararlar()

    @allure.story('Dava bilgileri sil')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.testcase('TESTCASE-16')
    def test_delete_case_information(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.decisions_tab_entry()
        case_details.delete_case_information()

    # Helper functions
    def login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email(self.df.loc[0,"username"])
        login.enter_password(self.df.loc[0,"pass"])
        login.click_login()