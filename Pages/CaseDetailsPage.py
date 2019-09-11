from Locators.locators_case_details import LocatorsCaseDetails
from Locators.locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class CaseDetails:

    RECEIVED_PAYMENT = "500000"
    RECEIVED_PAYMENT_DETAIL = "Bu ilk ödemedir. " \
                              "Daha sonraki ödemeler davanın " \
                              "seyrine göre değişecektir."
    DAY = "21"
    MONTH = "09"
    YEAR = "2019"

    EXPENSE_PAYMENT = "10000"
    EXPENSE_PAYMENT_DETAIL = "Davanın açılması için " \
                             "müvekkil yerine yapılan harcamalar"
    FILE_PATH = "C:/Users/z003d7tu/Desktop/ali.jPG"

    def __init__(self, driver):
        self.driver = driver
        self.table_last_row_xpath = LocatorsCaseDetails.table_last_row_xpath
        self.expense_tab_id = Locators.expense_tab_id
        self.tab_h4_title_class = LocatorsCaseDetails.tab_h4_title_class

        self.received_payment_txtbox_id = LocatorsCaseDetails.received_payment_txtbox_id
        self.received_payment_currency_dropbox_id = LocatorsCaseDetails.received_payment_currency_dropbox_id
        self.received_payment_detail_txtbox_id = LocatorsCaseDetails.received_payment_detail_txtbox_id
        self.received_payment_date_datetime_id = LocatorsCaseDetails.received_payment_date_datetime_id
        self.received_payment_add_btn_xpath = LocatorsCaseDetails.received_payment_add_btn_xpath

        self.expense_and_payment_div_id = LocatorsCaseDetails.expense_and_payment_div_id

        self.expense_txtbox_id = LocatorsCaseDetails.expense_txtbox_id
        self.expense_dropbox_id = LocatorsCaseDetails.expense_dropbox_id
        self.expense_detail_txtbox_id = LocatorsCaseDetails.expense_detail_txtbox_id
        self.expense_date_datetime_id = LocatorsCaseDetails.expense_date_datetime_id
        self.expense_add_btn_xpath = LocatorsCaseDetails.expense_add_btn_xpath

        self.add_new_evidence_btn_id = LocatorsCaseDetails.add_new_evidence_btn_id
        self.evidence_tab_id = Locators.evidence_tab_id
        self.add_new_evidence_file_btn_id = LocatorsCaseDetails.add_new_evidence_file_btn_id

    def expenses_tab_entry(self):
        # Select table last entry of table
        self.driver.find_element_by_xpath(self.table_last_row_xpath).click()
        self.driver.find_element_by_id(self.expense_tab_id).click()
        title = self.driver.find_element_by_class_name(self.tab_h4_title_class)
        assert title.text == "Masraflar & Alacaklar"

    def add_received_payment(self):
        self.driver.find_element_by_id(self.received_payment_txtbox_id).clear()
        self.driver.find_element_by_id(self.received_payment_txtbox_id).send_keys(self.RECEIVED_PAYMENT)
        select = Select(self.driver.find_element_by_id(self.received_payment_currency_dropbox_id))
        select.select_by_value('TL')
        self.driver.find_element_by_id(self.received_payment_detail_txtbox_id).clear()
        self.driver.find_element_by_id(self.received_payment_detail_txtbox_id).send_keys(self.RECEIVED_PAYMENT_DETAIL)
        self.driver.find_element_by_id(self.received_payment_date_datetime_id).click()
        self.driver.find_element_by_id(self.received_payment_date_datetime_id)\
            .send_keys(self.MONTH + self.DAY + self.YEAR)
        self.driver.find_element_by_xpath(self.received_payment_add_btn_xpath).click()

        # Find and store the received payments and expenses in "container" variable
        payment_detail = []
        container = self.driver.find_elements_by_id(self.expense_and_payment_div_id)
        for div_list in container:
            # After iteration of all div elements, find last element that you added
            div_items = div_list.find_elements_by_xpath('//*[@id="mtxk"]/div[last()]')
            for items in div_items:
                item = items.find_elements_by_xpath('//*[@id="mtxk"]/div[last()]/div')
                for i in item:
                    payment_detail.append(i.text)

        assert payment_detail[0] == self.RECEIVED_PAYMENT_DETAIL + ":"
        assert payment_detail[1] == self.YEAR + "-" + self.MONTH + "-" + self.DAY
        assert payment_detail[2] == self.RECEIVED_PAYMENT + ".00 TL"

    def add_expense(self):
        self.driver.find_element_by_id(self.expense_txtbox_id).clear()
        self.driver.find_element_by_id(self.expense_txtbox_id).send_keys(self.EXPENSE_PAYMENT)
        select = Select(self.driver.find_element_by_id(self.expense_dropbox_id))
        select.select_by_value('TL')
        self.driver.find_element_by_id(self.expense_detail_txtbox_id).clear()
        self.driver.find_element_by_id(self.expense_detail_txtbox_id).send_keys(self.EXPENSE_PAYMENT_DETAIL)
        self.driver.find_element_by_id(self.received_payment_date_datetime_id).send_keys(self.MONTH + self.DAY + self.YEAR)
        self.driver.find_element_by_xpath(self.expense_add_btn_xpath).click()

        expense_detail = []
        container = self.driver.find_elements_by_id(self.expense_and_payment_div_id)
        for div_list in container:
            # After iteration of all div elements,
            # find last element that you added
            div_items = div_list.find_elements_by_xpath('//*[@id="mtxk"]/div[last()]')
            for items in div_items:
                item = items.find_elements_by_xpath('//*[@id="mtxk"]/div[last()]/div')
                for i in item:
                    expense_detail.append(i.text)

        assert expense_detail[0] == self.EXPENSE_PAYMENT_DETAIL + ":"
        assert expense_detail[1] == self.YEAR + "-" + self.MONTH + "-" + self.DAY
        assert expense_detail[2] == self.EXPENSE_PAYMENT + ".00 TL"

    def evidence_tab_entry(self):
        # Select table last entry of table
        self.driver.find_element_by_xpath(self.table_last_row_xpath).click()
        self.driver.find_element_by_id(self.evidence_tab_id).click()
        title = self.driver.find_element_by_class_name(self.tab_h4_title_class)
        assert title.text == "Dosya Ekleri"

    def add_evidence(self):
        self.driver.find_element_by_id(self.add_new_evidence_btn_id).click()
        self.driver.find_element_by_id(self.add_new_evidence_file_btn_id).send_keys(self.FILE_PATH)

















