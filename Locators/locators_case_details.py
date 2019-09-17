
class LocatorsCaseDetails:

    table_last_row_xpath = "//a[contains(text(),'Law and Person interaction / Ali Pala -')]"
    tab_h4_title_class = "card-title"
    letter_of_application_h4_title_xpath = "//h4[@class='flex-grow-1 card-title']"

    # Expenses tab elements
    received_payment_txtbox_id = "alinanOdeme_rakam"
    received_payment_detail_txtbox_id = "alinanOdeme_detay"
    received_payment_date_datetime_id = "alinanOdeme_tarih"
    received_payment_currency_dropbox_id = "alinanOdeme_kur"
    received_payment_add_btn_xpath = "//button[@class='odeme btn btn-block btn-primary']"
    lawyer_fee_txtbox_id = "vekalet_ucreti_deger"
    lawyer_fee_currency_dropbox_name = "vekalet_ucreti_kur"
    lawyer_fee_fixed_radio_id = "sabit"
    lawyer_fee_percent_radio_id = "yuzde"
    lawyer_fee_percent_value_txtbox_id = "yuzde_degeri"
    total_received_payment_lbl_id = "toplam-alinacak-odeme"
    remaining_payment_lbl_id = "kalan-odeme"
    money_case_lbl_id = "kasa"
    expense_txtbox_id = "masraf_rakam"
    expense_dropbox_id = "masraf_kur"
    expense_detail_txtbox_id = "masraf_detay"
    expense_date_datetime_id = "masraf_tarih"
    expense_add_btn_xpath = "//button[@class='masraf px-5 btn btn-danger']"
    expense_submit_btn_name = "kaydet"
    expense_discard_btn_xpath = "//button[contains(text(),'PTAL ET')]"
    expense_and_payment_div_id = "mtxk"

    # Evidences tab elements
    add_new_evidence_btn_id = "yeni-delil-ekle"
    no_evidence_p_xpath = "//p[contains(text(),'Henüz bir delil eklemediniz.')]"
    evidence_delete_btn_xpath = "//i[@class='fas fa-trash']" # TODO Button locate method should be changed
    add_new_evidence_file_btn_id = "dosya-ekle-1"
    delete_evidence_attachment_btn_xpath = "//i[@class='fas fa-trash']"
    evidence_file_div_class_xpath = '//*[@id="delil-crd-1"]/div/div[2]/div/div'

    # Directive tab elements
    add_directive_btn_id = "btn-ibra_talimat-ekle"
    load_directive_btn_id = "btn-ibra_talimat-yukle"
    directive_delete_btn_xpath = "//i[@class='fas fa-trash']"
    directive_download_btn_xpath = "//i[@class='fas mr-2 fa-download']"
    directive_table_xpath = "//table[@class='table table-striped']//tbody"
    directive_delete_error_page_h1_xpath = '//*[@id="main-message"]/h1'
    ibra_radio_xpath = '//*[@id="ibra_talimat-ekle"]/div[1]/div/div[1]/div/label/input'
    ibra_talimat_title_txtbox_id = "ibra_talimat-input"
    ibra_talimat_detail_editor_id = "cke_1_contents"


    # Request tab elements
    add_request_btn_id = "dilekcele-ekle"
    load_request_btn_id = "dilekcele-yukle"
    select_request_dropbox_id = "dilekce-select"
    request_title_txtbox_id = "dilekce-input"
    # TODO rich text editor test
    request_save_btn_name = "kaydet"
    request_discard_btn_xpath = "//button[contains(text(),'PTAL ET')]"

    # "Dilekçeler" tab elements
    letter_of_application_save_btn_name = "kaydet"
    success_alert_message_xpath = "//div[@class='alert alert-success']"

    # Decisions tab elements
    file_type_dropbox_id = "tenzip-select"
    decisions_h4_title_xpath = "//h4[contains(text(),'Dava Bilgileri')]"

    # Kararlar/Ana kararlar elements
    case_type_dropbox_id = "tenzip-select"
    # "Tenzip zaptı" elements
    scan_copy_checkbox_name = "tenzip_tarama"
    tenzip_details_txtbox_name = "tenzip_aciklama[]"
    tenzip_end_date_checkbox_id = "son-tarih"
    tenzip_last_date_datetime_name = "tenzip_son_tarih"
    add_detail_plus_button_xpath = "//div[@id='aciklama']//button[@class='btn btn-sm btn-block'][contains(text(),'+')]"
    tenzip_table_type_xpath = '//*[@id="tenzip-table"]/div/table/tbody/tr[1]/th'
    tenzip_table_detail_xpath = '//*[@id="tenzip-table"]/div/table/tbody/tr[1]/td[5]'
    tenzip_save_btn_id = "arakarar-kayit"

    # "Duruşma günü elements"
    case_date_datetime_name = "durusma_gunu"
    durusma_details_txtbox_name = "durusma_aciklama[]"
    case_end_date_checkbox_id = "son-tarih-2"
    tenzip_add_details_plus_button_xpath = "//div[@id='aciklama']//button[@class='btn btn-sm btn-block'][contains(text(),'+')]"
    durusma_gunu_table_type_xpath = '//*[@id="tenzip-table"]/div/table/tbody/tr[2]/th'
    durusma_gunu_table_detail_xpath = '//*[@id="tenzip-table"]/div/table/tbody/tr[2]/td[5]'
    durusma_gunu_save_btn_id = "arakarar-kayit-2"

    # Sub decisions  elements
    decisions_date_datetime_name = "kararlar_tarih"
    decisions_scan_copy_checkbox_name = "kararlar_tarama_ornegi"
    kararlar_details_txtbox_name = "kararlar_aciklama[]"
    kararlar_add_details_plus_button_xpath = "//div[@id='aciklama-3']//button[@class='btn btn-sm btn-block'][contains(text(),'+')]"
    kararlar_end_date_checkbox_id = "son-tarih-3"
    kararlar_table_type_xpath = '//*[@id="tenzip-table"]/div/table/tbody/tr[3]/th'
    kararlar_table_detail_xpath = '//*[@id="tenzip-table"]/div/table/tbody/tr[3]/td[5]'
    kararlar_save_btn_id = "arakarar-kayit-3"

    # Delete case elements
    case_table_delete_btn_xpath = "//td[7]//a[1]"


