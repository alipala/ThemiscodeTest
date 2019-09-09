
class CaseDetails:

    # Expenses tab elements
    received_payment_txtbox_id = "alinanOdeme_rakam"
    received_payment_detail_txtbox_id = "alinanOdeme_detay"
    received_payment_date_datetime_id = "alinanOdeme_tarih"
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

    # Evidences tab elements
    add_new_evidence_btn_id = "yeni-delil-ekle"
    no_evidence_p_xpath = "//p[contains(text(),'Henüz bir delil eklemediniz.')]"
    evidence_delete_btn_xpath = "//i[@class='fas fa-trash']" # TODO Button locate method should be changed

    # Directive tab elements
    add_directive_btn_id = "btn-ibra_talimat-ekle"
    load_directive_btn_id = "btn-ibra_talimat-yukle"
    directive_delete_btn_xpath = "//i[@class='fas fa-trash']"
    directive_download_btn_xpath = "//i[@class='fas mr-2 fa-download']"

    # Request tab elements
    add_request_btn_id = "dilekcele-ekle"
    load_request_btn_id = "dilekcele-yukle"
    select_request_dropbox_id = "dilekce-select"
    request_title_txtbox_id = "dilekce-input"
    # TODO rich text edito test
    request_save_btn_name = "kaydet"
    request_discard_btn_xpath = "//button[contains(text(),'PTAL ET')]"

    # Decisions tab elements
    file_type_dropbox_id = "tenzip-select"
    file_type_h4_title_class = "card-title"
    # "Tenzip zaptı" elements
    scan_copy_checkbox_name = "tenzip_tarama"
    tenzip_details_txtbox_name = "tenzip_aciklama[]"
    tenzip_end_date_checkbox_id = "son-tarih"
    add_detail_plus_button_xpath = "//div[@id='aciklama']//button[@class='btn btn-sm btn-block'][contains(text(),'+')]"
    # "Duruşma günü elements"
    case_date_datetime_name = "durusma_gunu"
    durusma_details_txtbox_name = "durusma_aciklama[]"
    case_end_date_checkbox_id = "son-tarih-2"
    tenzip_add_details_plus_button_xpath = "//div[@id='aciklama']//button[@class='btn btn-sm btn-block'][contains(text(),'+')]"
    # Sub decisions  elements
    decisions_date_datetime_name = "kararlar_tarih"
    decisions_scan_copy_checkbox_name = "kararlar_tarama_ornegi"
    kararlar_details_txtbox_name = "kararlar_aciklama[]"
    kararlar_add_details_plus_button_xpath = "//div[@id='aciklama-3']//button[@class='btn btn-sm btn-block'][contains(text(),'+')]"
    kararlar_end_date_checkbox_id = "son-tarih-3"

