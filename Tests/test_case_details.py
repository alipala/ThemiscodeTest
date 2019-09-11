import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from Pages.CaseDetailsPage import CaseDetails
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Base.base import Base
import pandas as pd


class TestCaseDetails(Base):
    __user_data_file = r"\login_details.xlsx"
    df = pd.read_excel(os.getcwd() + __user_data_file)

    # def test_go_expenses_tab(self):
    #     driver = self.driver
    #     self.login()
    #     case_details = CaseDetails(driver)
    #     home = HomePage(driver)
    #     home.click_law_suit_page()
    #     case_details.expenses_tab_entry()

    # def test_add_received_payment(self):
    #     driver = self.driver
    #     self.login()
    #     case_details = CaseDetails(driver)
    #     home = HomePage(driver)
    #     home.click_law_suit_page()
    #     case_details.expenses_tab_entry()
    #     case_details.add_received_payment()

    # def test_add_expense(self):
    #     driver = self.driver
    #     self.login()
    #     case_details = CaseDetails(driver)
    #     home = HomePage(driver)
    #     home.click_law_suit_page()
    #     case_details.expenses_tab_entry()
    #     case_details.add_expense()

    def test_add_evidence(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.evidence_tab_entry()
        case_details.add_evidence_attachment()

    def test_delete_evidence(self):
        driver = self.driver
        self.login()
        case_details = CaseDetails(driver)
        home = HomePage(driver)
        home.click_law_suit_page()
        case_details.evidence_tab_entry()
        case_details.delete_evidence_attachment()




    # Helper functions
    def login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_email(self.df.loc[0,"username"])
        login.enter_password(self.df.loc[0,"pass"])
        login.click_login()