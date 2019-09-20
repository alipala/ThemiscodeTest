from Locators.locators_case_details import LocatorsCaseDetails
from Locators.locators import Locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import allure


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
    FILE_PATH_IMAGE = "C:/Users/z003d7tu/Desktop/ali.jPG"
    FILE_PATH_PDF = "C:/Users/z003d7tu/Desktop/big-o-cheatsheet.pdf"
    FILE_PATH_EXCEL = "C:/Users/z003d7tu/Desktop/SSK.xlsx"
    IBRA_TITLE = "İbra Örneği"
    IBRA_DETAIL = "Bu bir ibra örneğidir ve robot tarafından " \
                  "ibraz edilerek test amaçlı yazılmıştır. "
    TALIMAT_TITLE = "Talimat Örneği"
    LETTER_OF_APPLICATION_TITLE = "Bu bir örnek trafik kazası başlığıdır."
    EDITED_LETTER_OF_APPLICATION_TITLE = "Bu bir Tasarrufun İptali Cevap Dilekçesidir"
    TENZIP_ZAPTI_DETAIL = "Bu örnek bir tenzip zaptıdır."
    DURUSMA_GUNU_DETAIL = "Duruşma gününü kaçırmamak gerek mazallah"
    KARARLAR_DETAIL = "Alınan kararların detaylarını burada görebiliriz."

    # Locators initialization
    def __init__(self, driver):
        self.driver = driver
        self.table_last_row_xpath = LocatorsCaseDetails.table_last_row_xpath
        self.expense_tab_id = Locators.expense_tab_id
        self.tab_h4_title_class = LocatorsCaseDetails.tab_h4_title_class
        self.letter_of_application_h4_title_xpath = LocatorsCaseDetails.letter_of_application_h4_title_xpath

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
        self.delete_evidence_attachment_btn_xpath = LocatorsCaseDetails.delete_evidence_attachment_btn_xpath
        self.evidence_file_div_class_pdf_xpath = LocatorsCaseDetails.evidence_file_div_class_pdf_xpath
        self.evidence_file_div_class_xls_xpath = LocatorsCaseDetails.evidence_file_div_class_xls_xpath

        self.directive_table_xpath = LocatorsCaseDetails.directive_table_xpath
        self.request_tab_id = Locators.request_tab_id
        self.directive_delete_error_page_h1_xpath = LocatorsCaseDetails.directive_delete_error_page_h1_xpath
        self.load_directive_btn_id = LocatorsCaseDetails.load_directive_btn_id
        self.add_directive_btn_id = LocatorsCaseDetails.add_directive_btn_id
        self.ibra_radio_xpath = LocatorsCaseDetails.ibra_radio_xpath
        self.ibra_talimat_title_txtbox_id = LocatorsCaseDetails.ibra_talimat_title_txtbox_id
        self.ibra_talimat_detail_editor_id = LocatorsCaseDetails.ibra_talimat_detail_editor_id
        self.request_save_btn_name = LocatorsCaseDetails.request_save_btn_name

        self.letter_of_application_id = Locators.letter_of_application_id
        self.add_request_btn_id = LocatorsCaseDetails.add_request_btn_id
        self.select_request_dropbox_id = LocatorsCaseDetails.select_request_dropbox_id
        self.request_title_txtbox_id = LocatorsCaseDetails.request_title_txtbox_id
        self.letter_of_application_save_btn_name = LocatorsCaseDetails.letter_of_application_save_btn_name
        self.success_alert_message_xpath = LocatorsCaseDetails.success_alert_message_xpath

        self.decisions_tab_id = Locators.decisions_tab_id
        self.decisions_h4_title_xpath = LocatorsCaseDetails.decisions_h4_title_xpath
        self.case_type_dropbox_id = LocatorsCaseDetails.case_type_dropbox_id
        self.tenzip_details_txtbox_name = LocatorsCaseDetails.tenzip_details_txtbox_name
        self.tenzip_end_date_checkbox_id = LocatorsCaseDetails.tenzip_end_date_checkbox_id
        self.scan_copy_checkbox_name = LocatorsCaseDetails.scan_copy_checkbox_name
        self.tenzip_last_date_datetime_name = LocatorsCaseDetails.tenzip_last_date_datetime_name
        self.tenzip_table_type_xpath = LocatorsCaseDetails.tenzip_table_type_xpath
        self.tenzip_table_detail_xpath = LocatorsCaseDetails.tenzip_table_detail_xpath
        self.tenzip_save_btn_id = LocatorsCaseDetails.tenzip_save_btn_id

        self.case_date_datetime_name = LocatorsCaseDetails.case_date_datetime_name
        self.durusma_details_txtbox_name = LocatorsCaseDetails.durusma_details_txtbox_name
        self.case_end_date_checkbox_id = LocatorsCaseDetails.case_end_date_checkbox_id
        self.tenzip_add_details_plus_button_xpath = LocatorsCaseDetails.tenzip_add_details_plus_button_xpath
        self.durusma_gunu_table_type_xpath = LocatorsCaseDetails.durusma_gunu_table_type_xpath
        self.durusma_gunu_table_detail_xpath = LocatorsCaseDetails.durusma_gunu_table_detail_xpath
        self.durusma_gunu_save_btn_id = LocatorsCaseDetails.durusma_gunu_save_btn_id

        self.decisions_date_datetime_name = LocatorsCaseDetails.decisions_date_datetime_name
        self.decisions_scan_copy_checkbox_name = LocatorsCaseDetails.decisions_scan_copy_checkbox_name
        self.kararlar_details_txtbox_name = LocatorsCaseDetails.kararlar_details_txtbox_name
        self.kararlar_add_details_plus_button_xpath = LocatorsCaseDetails.kararlar_add_details_plus_button_xpath
        self.kararlar_end_date_checkbox_id = LocatorsCaseDetails.kararlar_end_date_checkbox_id
        self.kararlar_table_type_xpath = LocatorsCaseDetails.kararlar_table_type_xpath
        self.kararlar_table_detail_xpath = LocatorsCaseDetails.kararlar_table_detail_xpath
        self.kararlar_save_btn_id = LocatorsCaseDetails.kararlar_save_btn_id

        self.case_table_delete_btn_xpath = LocatorsCaseDetails.case_table_delete_btn_xpath

    def expenses_tab_entry(self):
        driver = self.driver
        self.workaround_table_list_entries()
        # Select table last entry of table
        self.driver.find_element_by_xpath(self.table_last_row_xpath).click()
        self.driver.find_element_by_id(self.expense_tab_id).click()
        title = self.driver.find_element_by_class_name(self.tab_h4_title_class)
        # Allure screenshot for the test
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        assert title.text == "Masraflar & Alacaklar"

    def add_received_payment(self):
        driver = self.driver
        self.driver.find_element_by_id(self.received_payment_txtbox_id).clear()
        self.driver.find_element_by_id(self.received_payment_txtbox_id).send_keys(self.RECEIVED_PAYMENT)
        select = Select(self.driver.find_element_by_id(self.received_payment_currency_dropbox_id))
        select.select_by_value('TL')
        self.driver.find_element_by_id(self.received_payment_detail_txtbox_id).clear()
        self.driver.find_element_by_id(self.received_payment_detail_txtbox_id).send_keys(self.RECEIVED_PAYMENT_DETAIL)
        # Another Solution 1
        # datefield = self.driver.find_element_by_id(self.received_payment_date_datetime_id)
        # ActionChains(self.driver).move_to_element(datefield).click()\
        #     .send_keys(self.MONTH + self.DAY + self.YEAR).perform()
        # Another Solution 2
        self.driver.find_element_by_id(self.received_payment_date_datetime_id).clear()
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
        # Allure screenshot for the test
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)

        for i in range(3):
            print(payment_detail[i])
        assert payment_detail[0] == self.RECEIVED_PAYMENT_DETAIL + ":"
        assert payment_detail[1] == self.YEAR + "-" + self.MONTH + "-" + self.DAY
        assert payment_detail[2] == self.RECEIVED_PAYMENT + ".00 TL"

    def add_expense(self):
        driver = self.driver
        self.driver.find_element_by_id(self.expense_txtbox_id).clear()
        self.driver.find_element_by_id(self.expense_txtbox_id).send_keys(self.EXPENSE_PAYMENT)
        select = Select(self.driver.find_element_by_id(self.expense_dropbox_id))
        select.select_by_value('TL')
        self.driver.find_element_by_id(self.expense_detail_txtbox_id).clear()
        self.driver.find_element_by_id(self.expense_detail_txtbox_id).send_keys(self.EXPENSE_PAYMENT_DETAIL)
        self.driver.find_element_by_id(self.expense_date_datetime_id).clear()
        self.driver.find_element_by_id(self.expense_date_datetime_id).send_keys(self.MONTH + self.DAY + self.YEAR)
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
        # Allure screenshot for the test
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        assert expense_detail[0] == self.EXPENSE_PAYMENT_DETAIL + ":"
        assert expense_detail[1] == self.YEAR + "-" + self.MONTH + "-" + self.DAY
        assert expense_detail[2] == self.EXPENSE_PAYMENT + ".00 TL"

    def evidence_tab_entry(self):
        self.workaround_table_list_entries()
        # Select table last entry of table
        self.driver.find_element_by_xpath(self.table_last_row_xpath).click()
        self.driver.find_element_by_id(self.evidence_tab_id).click()
        title = self.driver.find_element_by_class_name(self.tab_h4_title_class)
        assert title.text == "Dosya Ekleri"

    def add_evidence_attachment_image(self):
        driver = self.driver
        self.driver.find_element_by_id(self.add_new_evidence_btn_id).click()
        attach_index = "1"
        self.driver.find_element_by_id(self.add_new_evidence_file_btn_id + attach_index).send_keys(self.FILE_PATH_IMAGE)
        time.sleep(2)
        try:
            img_list = []
            source = self.driver.find_elements_by_tag_name('img')
            for image in source:
                img_list.append(image.get_attribute('src'))
            img_link = img_list[1]
            self.driver.get(img_link)
            img_title = img_link[37:]
            # Allure screenshot for the test
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
            assert img_title in self.driver.title
        except Exception as e:
            raise e

    def add_evidence_attachment_pdf(self):
        driver = self.driver
        self.driver.find_element_by_id(self.add_new_evidence_btn_id).click()
        attach_index = "2"
        self.driver.find_element_by_id(self.add_new_evidence_file_btn_id + attach_index).send_keys(self.FILE_PATH_PDF)
        time.sleep(2)
        try:
            div = self.driver.find_element_by_xpath(self.evidence_file_div_class_pdf_xpath)
            pdf_link = div.find_element_by_css_selector('a').get_attribute('href')
            pdf = pdf_link[37:]
            # Allure screenshot for the test
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
            assert ".pdf" in pdf
        except Exception as e:
            raise e

    def add_evidence_attachment_excel(self):
        driver = self.driver
        self.driver.find_element_by_id(self.add_new_evidence_btn_id).click()
        attach_index = "3"
        self.driver.find_element_by_id(self.add_new_evidence_file_btn_id + attach_index).send_keys(self.FILE_PATH_EXCEL)
        time.sleep(2)
        try:
            div = self.driver.find_element_by_xpath(self.evidence_file_div_class_xls_xpath)
            excel_link = div.find_element_by_css_selector('a').get_attribute('href')
            self.driver.get(excel_link)
            print(self.driver.title)
            # Allure screenshot for the test
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
            assert "404 Page Not Found" != self.driver.title
        except Exception as e:
            raise e

    def delete_evidence_attachment(self):
        driver = self.driver
        # There are 3 attachments to be deleted
        for i in range(3):
            self.driver.find_element_by_xpath(self.delete_evidence_attachment_btn_xpath).click()
            time.sleep(2)
            # TODO: Tell developers There should be a warning popup
            assert "There should be a warning" == "There should be a warning"
        # Allure screenshot for the test
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)

    def request_tab_entry(self):
        self.workaround_table_list_entries()
        self.driver.find_element_by_xpath(self.table_last_row_xpath).click()
        self.driver.find_element_by_id(self.request_tab_id).click()
        title = self.driver.find_element_by_class_name(self.tab_h4_title_class)
        assert title.text == "İbralar/Talimatlar"

    # TODO: Handle file upload
    # def load_request(self):
    #     self.driver.find_element_by_id(self.load_directive_btn_id).click()

    def delete_loaded_request(self):
        # Locate delete button of the first row element.
        delete_btn = self.driver.find_element_by_xpath("//table/tbody/tr[1]/td[4]/a[2]")
        delete_btn.click()
        assert self.driver.title != "404 Page Not Found"

    def add_request(self):
        driver = self.driver
        self.driver.find_element_by_id(self.add_directive_btn_id).click()
        # Select first radio
        is_selected = self.driver.find_element_by_xpath(self.ibra_radio_xpath).get_attribute("checked")
        assert is_selected is not None
        title_textbox = self.driver.find_element_by_id(self.ibra_talimat_title_txtbox_id)
        title_textbox.send_keys(self.IBRA_TITLE)
        assert title_textbox.get_attribute('value') == self.IBRA_TITLE
        self.ckeditor_handling()
        self.driver.find_element_by_name(self.request_save_btn_name).click()
        # Allure screenshot for the test
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)

    def delete_added_request(self):
        driver = self.driver
        # Locate delete button of the second row element.
        delete_btn = self.driver.find_element_by_xpath("//table/tbody/tr/td[4]/a[2]")
        delete_btn.click()
        h1 = self.driver.find_element_by_xpath(self.directive_delete_error_page_h1_xpath)
        # Allure screenshot for the test
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        assert h1.text != "This page isn’t working"


    def letter_of_application_tab_entry(self):
        self.workaround_table_list_entries()
        self.driver.find_element_by_xpath(self.table_last_row_xpath).click()
        self.driver.find_element_by_id(self.letter_of_application_id).click()
        title = self.driver.find_element_by_xpath(self.letter_of_application_h4_title_xpath)
        assert title.text == "Dilekçeler"

    def add_letter_of_application(self):
        driver = self.driver
        self.driver.find_element_by_id(self.add_request_btn_id).click()
        select = Select(self.driver.find_element_by_id(self.select_request_dropbox_id))
        select.select_by_index(1)
        selected_option = select.first_selected_option
        assert selected_option.text == "Araba Kazası Maddi Mazminat Dava Dilekçesi"

        self.driver.find_element_by_id(self.request_title_txtbox_id).send_keys(self.LETTER_OF_APPLICATION_TITLE)
        self.driver.find_element_by_name(self.letter_of_application_save_btn_name).click()
        alert = self.driver.find_element_by_xpath(self.success_alert_message_xpath)
        assert alert.text == "Dilekçe başarıyla eklendi."
        # Allure screenshot for the test
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)

    def edit_letter_of_application(self):
        driver = self.driver
        # Edit last row of the table clicking edit icon
        edit_btn = self.driver.find_element_by_xpath("//table/tbody/tr[1]/td[4]/a[1]")
        edit_btn.click()
        select = Select(self.driver.find_element_by_id(self.select_request_dropbox_id))
        select.select_by_index(11)
        self.driver.find_element_by_id(self.request_title_txtbox_id).clear()
        self.driver.find_element_by_id(self.request_title_txtbox_id).send_keys(self.LETTER_OF_APPLICATION_TITLE)
        self.driver.find_element_by_name(self.letter_of_application_save_btn_name).click()

        # Get last row of the table
        letter_name = self.driver.find_element_by_xpath("//table[1]/tbody/tr[1]/td[1]")
        print(letter_name.text)
        # Allure screenshot for the test
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        assert letter_name.text == "Tasarrufun İptali Cevap Dilekçesi"

    def delete_letter_of_application(self):
        driver = self.driver
        # Delete last row of the table clicking delete icon
        delete_btn = self.driver.find_element_by_xpath("//table/tbody/tr[1]/td[4]/a[2]")
        delete_btn.click()
        alert = self.driver.find_element_by_xpath(self.success_alert_message_xpath)
        # Allure screenshot for the test
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        assert alert.text == "Dilekçe başarıyla silindi."

    # TODO: Handle file upload
    # def load_letter_of_application(self):
    #     pass

    def decisions_tab_entry(self):
        self.workaround_table_list_entries()
        self.driver.find_element_by_xpath(self.table_last_row_xpath).click()
        self.driver.find_element_by_id(self.decisions_tab_id).click()
        h4_title = self.driver.find_element_by_xpath(self.decisions_h4_title_xpath)
        assert h4_title.text == "Dava Bilgileri"

    def add_tenzip_zapti(self):
        driver = self.driver
        select = Select(self.driver.find_element_by_id(self.case_type_dropbox_id))
        select.select_by_index(1)
        self.driver.find_element_by_name(self.scan_copy_checkbox_name).click()
        txtbox = self.driver.find_element_by_name(self.tenzip_details_txtbox_name)
        txtbox.clear()
        txtbox.send_keys(self.TENZIP_ZAPTI_DETAIL)
        self.driver.find_element_by_id(self.tenzip_end_date_checkbox_id).click()
        self.driver.find_element_by_name(self.tenzip_last_date_datetime_name)\
            .send_keys(self.MONTH + self.DAY + self.YEAR)
        # Save tenzip
        self.driver.find_element_by_id(self.tenzip_save_btn_id).click()
        time.sleep(2)
        tenzip_type = self.driver.find_element_by_xpath(self.tenzip_table_type_xpath)
        tenzip_detail = self.driver.find_element_by_xpath(self.tenzip_table_detail_xpath)
        # Allure screenshot for the test
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        assert tenzip_type.text == "Tenzip Zaptı"
        assert tenzip_detail.text == self.TENZIP_ZAPTI_DETAIL
        # + BUTONU UNUTUMA

    def add_durusma_gunu(self):
        driver = self.driver
        select = Select(self.driver.find_element_by_id(self.case_type_dropbox_id))
        select.select_by_index(2)
        self.driver.find_element_by_name(self.case_date_datetime_name)\
            .send_keys(self.MONTH + self.DAY + self.YEAR)
        txtbox = self.driver.find_element_by_name(self.durusma_details_txtbox_name)
        txtbox.clear()
        txtbox.send_keys(self.DURUSMA_GUNU_DETAIL)
        self.driver.find_element_by_id(self.case_end_date_checkbox_id).click()
        # Save duruşma günü
        self.driver.find_element_by_id(self.durusma_gunu_save_btn_id).click()
        time.sleep(2)
        durusma_gunu_type = self.driver.find_element_by_xpath(self.durusma_gunu_table_type_xpath)
        durusma_gunu_detail = self.driver.find_element_by_xpath(self.durusma_gunu_table_detail_xpath)
        # Allure screenshot for the test
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        assert durusma_gunu_type.text == "Duruşma Günü"
        assert durusma_gunu_detail.text == self.DURUSMA_GUNU_DETAIL


    def add_kararlar(self):
        driver = self.driver
        select = Select(self.driver.find_element_by_id(self.case_type_dropbox_id))
        select.select_by_index(3)
        self.driver.find_element_by_name(self.decisions_date_datetime_name).send_keys(self.MONTH + self.DAY + self.YEAR)
        self.driver.find_element_by_name(self.decisions_scan_copy_checkbox_name).click()
        txtbox = self.driver.find_element_by_name(self.kararlar_details_txtbox_name)
        txtbox.clear()
        txtbox.send_keys(self.KARARLAR_DETAIL)
        self.driver.find_element_by_id(self.kararlar_end_date_checkbox_id).click()
        # Save kararlar
        self.driver.find_element_by_id(self.kararlar_save_btn_id).click()
        time.sleep(2)
        kararlar_type = self.driver.find_element_by_xpath(self.kararlar_table_type_xpath)
        kararlar_detail = self.driver.find_element_by_xpath(self.kararlar_table_detail_xpath)
        # Allure screenshot for the test
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        assert kararlar_type.text == "Karar"
        assert kararlar_detail.text == self.KARARLAR_DETAIL

    def delete_case_information(self):
        driver = self.driver
        for i in range(1, 4):
            if i == 3:
                tr = "//tr"
            else:
                tr = "//tr[" + str(i) + "]"
            btn_xpath = tr + self.case_table_delete_btn_xpath
            self.driver.find_element_by_xpath(btn_xpath).click()
        # Allure screenshot for the test
        allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)

    # Helper functions
    def ckeditor_handling(self):
        result = False
        attempt = 0
        while attempt < 2:
            try:
                # ckeditor body xpath: https://bangladroid.wordpress.com/2016/08/20/switch-to-ckeditor-in-selenium-python/
                basic_page_body_xpath = "//div[contains(@id, 'cke_1_contents')]/iframe"
                ckeditor_frame = self.driver.find_element_by_xpath(basic_page_body_xpath)

                # Switch to iframe
                self.driver.switch_to.frame(ckeditor_frame)

                # Send key to Ckeditor Body
                editor_body = self.driver.find_element_by_xpath("//body")
                editor_body.send_keys(self.IBRA_DETAIL)

                # if driver is already inside ckeditor_frame, switch out first
                self.driver.switch_to_default_content()


                result = True
            except Exception as e:
                raise e

            attempt += 1
        return result

    # Dava dosyaları table does not filled immediately into page.
    # Because of this problem, it is a workaround solution
    def workaround_table_list_entries(self):
        select = Select(self.driver.find_element_by_name(Locators.data_records_dropbox_name))
        select.select_by_value('25')
        time.sleep(15)

















