from Locators.locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


class LawsuitPage:

    CASE_SUBJECT = "Law and Person interaction"
    CITY_REGION = "Pendik"
    CASE_CREATE_DATE = "09082019"
    COURT_NAME = "İZMİR"
    SHEET_NO = "9000"
    CASE_VALUE = "100000"
    EXTRA_YEAR = "2019"
    EXTRA_NO = "023"
    DECISION_YEAR = "2019"
    DECISION_YEAR_NO = "0023"
    DECISION_DATE = "2019"
    DECISION_DATE_NO = "678"
    CASE_FINAL_DATE = "2020"
    CLIENT_NAME = "Ali Pala"
    CLIENT_CITIZEN_NO = "98765432768"
    CLIENT_TEL_NO = "0905442345667"
    CLIENT_ADDRESS = 'İçerenköy Mahallesi ' \
                     'Eski üsküdar yolu cad. Ataşehir'

    DEFENDANT_NAME = "Selim Cihantuna"
    DEFENDANT_CITIZEN_NO = "23569632568"
    DEFENDANT_TEL_NO = "+900256896521"
    DEFENDANT_ADDRESS = 'Dumlupınar Mah. Şehit ' \
                        'Hasan Kurt Sok No: 34'

    DETAILS = 'Dava hakkındaki detaylar buraya gelecek. ' \
              'Her iki taraf dinlendikten sonra avukat ' \
              'hatırlamak için bu kısımları doldurabilir.'

    def __init__(self, driver):
        self.driver = driver
        self.table_last_row_xpath = Locators.table_last_row_xpath
        self.case_create_btn_id = Locators.case_create_btn_id
        self.case_type_dropbox_id = Locators.case_type_dropbox_id
        self.case_type_detail_dropbox_id = Locators.case_type_detail_dropbox_id
        self.case_subject_txtbox_id = Locators.case_subject_txtbox_id
        self.case_city_dropbox_id = Locators.case_city_dropbox_id
        self.case_city_region_txtbox_id = Locators.case_city_region_txtbox_id
        self.case_create_date_time_picker_id = Locators.case_create_date_time_picker_id
        self.court_no_dropbox_id = Locators.court_no_dropbox_id
        self.court_name_txtbox_id = Locators.court_name_txtbox_id
        self.case_status_dropbox_id = Locators.case_status_dropbox_id
        self.sheet_no_txtbox_id = Locators.sheet_no_txtbox_id
        self.case_value_txtbox_id = Locators.case_value_txtbox_id
        self.case_value_currency_dropbox_id = Locators.case_value_currency_dropbox_id
        self.case_extra_year_txtbox_id = Locators.case_extra_year_txtbox_id
        self.case_extra_no_txtbox_id = Locators.case_extra_no_txtbox_id
        self.case_decision_year_txtbox_id = Locators.case_decision_year_txtbox_id
        self.case_decision_year_no_txtbox_id = Locators.case_decision_year_no_txtbox_id
        self.case_decision_date_txtbox_id = Locators.case_decision_date_txtbox_id
        self.case_decision_date_no_txtbox_id = Locators.case_decision_date_no_txtbox_id
        self.case_final_date_txtbox_id = Locators.case_final_date_txtbox_id
        self.case_add_btn_id = Locators.case_add_btn_id

        self.client_type_person_radio_css = Locators.client_type_person_radio_css
        self.client_is_adult_radio_css = Locators.client_is_adult_radio_css
        self.client_case_davaci_radio_css = Locators.client_case_davaci_radio_css
        self.client_name_txtbox_name = Locators.client_name_txtbox_name
        self.client_citizen_no_txtbox_name = Locators.client_citizen_no_txtbox_name
        self.client_tel_no_txtbox_id = Locators.client_tel_no_txtbox_id
        self.client_address_txtarea_id = Locators.client_address_txtarea_id
        self.client_add_btn_id = Locators.client_add_btn_id

        self.defendant_type_person_radio_css = Locators.defendant_type_person_radio_css
        self.defendant_is_adult_radio_css = Locators.defendant_is_adult_radio_css
        self.defendant_case_davaci_radio_css = Locators.defendant_case_davaci_radio_css
        self.defendant_name_txtbox_name = Locators.defendant_name_txtbox_name
        self.defendant_citizen_no_txtbox_name = Locators.defendant_citizen_no_txtbox_name
        self.defendant_tel_no_txtbox_id = Locators.defendant_tel_no_txtbox_id
        self.defendant_address_txtarea_id = Locators.defendant_address_txtarea_id
        self.defendant_add_btn_id = Locators.defendant_add_btn_id

        self.case_details_notes_txtarea_name = Locators.case_details_notes_txtarea_name
        self.lawyer_dropbox_css = Locators.lawyer_dropbox_css
        self.lawyer_add_btn_css = Locators.lawyer_add_btn_css
        self.additional_lawyer_dropbox_css = Locators.additional_lawyer_dropbox_css
        self.submit_btn_name = Locators.submit_btn_name
        self.discard_btn_css = Locators.discard_btn_css

        self.case_edit_information_btn_xpath = Locators.case_edit_information_btn_xpath

    def click_case_create_btn(self):
        self.driver.find_element_by_id(self.case_create_btn_id).click()

    def fill_case_information(self):
        select = Select(self.driver.find_element_by_id(self.case_type_dropbox_id))
        select.select_by_value('Ceza')

        select = Select(self.driver.find_element_by_id(self.case_type_detail_dropbox_id))
        select.select_by_value(('Asliye Ceza'))

        self.driver.find_element_by_id(self.case_subject_txtbox_id).send_keys(self.CASE_SUBJECT)

        select = Select(self.driver.find_element_by_id(self.case_city_dropbox_id))
        select.select_by_index(2)

        self.driver.find_element_by_id(self.case_city_region_txtbox_id).send_keys(self.CITY_REGION)

        # TODO Date picker test will be implemented by using DatePicker element rather than send_keys
        datefield = self.driver.find_element_by_id(self.case_create_date_time_picker_id)
        ActionChains(self.driver).move_to_element(datefield).click().send_keys(self.CASE_CREATE_DATE).perform()

        select = Select(self.driver.find_element_by_id(self.court_no_dropbox_id))
        select.select_by_value('0')

        self.driver.find_element_by_id(self.court_name_txtbox_id).send_keys(self.COURT_NAME)

        select = Select(self.driver.find_element_by_id(self.case_status_dropbox_id))
        select.select_by_value('Derdest')

        self.driver.find_element_by_id(self.sheet_no_txtbox_id).send_keys(self.SHEET_NO)

        self.driver.find_element_by_id(self.case_value_txtbox_id).send_keys(self.CASE_VALUE)

        select = Select(self.driver.find_element_by_id(self.case_value_currency_dropbox_id))
        select.select_by_value('USD')

        self.driver.find_element_by_id(self.case_extra_year_txtbox_id).send_keys(self.EXTRA_YEAR)

        self.driver.find_element_by_id(self.case_extra_no_txtbox_id).send_keys(self.EXTRA_NO)

        self.driver.find_element_by_id(self.case_decision_year_txtbox_id).send_keys(self.DECISION_YEAR)

        self.driver.find_element_by_id(self.case_decision_year_no_txtbox_id).send_keys(self.DECISION_YEAR_NO)

        self.driver.find_element_by_id(self.case_decision_date_txtbox_id).send_keys(self.DECISION_DATE)

        self.driver.find_element_by_id(self.case_decision_date_no_txtbox_id).send_keys(self.DECISION_DATE_NO)

        self.driver.find_element_by_id(self.case_final_date_txtbox_id).send_keys(self.CASE_FINAL_DATE)

        self.driver.find_element_by_id(self.case_add_btn_id).click()

    def fill_client_information(self):
        # First radio
        self.driver.find_element_by_css_selector(self.client_type_person_radio_css).click
        is_selected = self.driver.find_element_by_css_selector(self.client_type_person_radio_css).get_attribute("checked")
        try:
            assert is_selected is not None
            print("Element checked - ", is_selected)
        except Exception:
            raise
            print("Element checked - false")

        # Second radio
        self.driver.find_element_by_css_selector(self.client_is_adult_radio_css).click()
        is_selected = self.driver.find_element_by_css_selector(self.client_is_adult_radio_css).get_attribute("checked")
        try:
            assert is_selected is not None
            print("Element checked - ", is_selected)
        except Exception:
            raise
            print("Element checked - false")

        # Third radio
        self.driver.find_element_by_css_selector(self.client_case_davaci_radio_css).click()
        is_selected = self.driver.find_element_by_css_selector(self.client_case_davaci_radio_css).get_attribute("checked")
        try:
            assert is_selected is not None
            print("Element checked - ", is_selected)
        except Exception:
            raise
            print("Element checked - false")

        self.driver.find_element_by_name(self.client_name_txtbox_name).send_keys(self.CLIENT_NAME)

        self.driver.find_element_by_name(self.client_citizen_no_txtbox_name).send_keys(self.CLIENT_CITIZEN_NO)

        self.driver.find_element_by_id(self.client_tel_no_txtbox_id).send_keys(self.CLIENT_TEL_NO)

        self.driver.find_element_by_id(self.client_address_txtarea_id).send_keys(self.CLIENT_ADDRESS)

        self.driver.find_element_by_id(self.client_add_btn_id).click()

    def fill_defendant_information(self):
        # First radio
        self.driver.find_element_by_css_selector(self.defendant_type_person_radio_css).click
        is_selected = self.driver.find_element_by_css_selector(self.defendant_type_person_radio_css).get_attribute("checked")
        try:
            assert is_selected is not None
            print("Element checked - ", is_selected)
        except Exception:
            raise
            print("Element checked - false")

        # Second radio
        self.driver.find_element_by_css_selector(self.defendant_is_adult_radio_css).click()
        is_selected = self.driver.find_element_by_css_selector(self.defendant_is_adult_radio_css).get_attribute("checked")
        try:
            assert is_selected is not None
            print("Element checked - ", is_selected)
        except Exception:
            raise
            print("Element checked - false")

        # Third radio
        self.driver.find_element_by_css_selector(self.defendant_case_davaci_radio_css).click()
        is_selected = self.driver.find_element_by_css_selector(self.defendant_case_davaci_radio_css).get_attribute("checked")
        try:
            assert is_selected is not None
            print("Element checked - ", is_selected)
        except Exception:
            raise
            print("Element checked - false")

        self.driver.find_element_by_name(self.defendant_name_txtbox_name).send_keys(self.CLIENT_NAME)

        self.driver.find_element_by_name(self.defendant_citizen_no_txtbox_name).send_keys(self.CLIENT_CITIZEN_NO)

        self.driver.find_element_by_id(self.defendant_tel_no_txtbox_id).send_keys(self.CLIENT_TEL_NO)

        self.driver.find_element_by_id(self.defendant_address_txtarea_id).send_keys(self.CLIENT_ADDRESS)

        self.driver.find_element_by_id(self.defendant_add_btn_id).click()

    def fill_details(self):
        self.driver.find_element_by_name(self.case_details_notes_txtarea_name).send_keys(self.DETAILS)

        select = Select(self.driver.find_element_by_css_selector(self.lawyer_dropbox_css))
        select.select_by_value('1')

        self.driver.find_element_by_css_selector(self.lawyer_add_btn_css).click()

        # TODO wait until visible
        select = Select(self.driver.find_element_by_css_selector(self.additional_lawyer_dropbox_css))
        select.select_by_value('21')

    def save_case(self):
        self.driver.find_element_by_name(self.submit_btn_name).click()

    def discard_case(self):
        self.driver.find_element_by_css_selector(self.discard_btn_css).click()

    def select_table_last_entry(self):
        self.driver.find_element_by_xpath(self.table_last_row_xpath).click()

    def case_entry_information_edit(self):
        pass






