
class Locators:

    # LoginPage elements
    email_txtbox_name = "email"
    pass_txtbox_name = "password"
    login_btn_name = "send"

    # HomePage elements
    logout_link_xpath = "//a[@href='http://themiscode.com/panel/General/logout']"
    user_partial_link_text = "Hoşgeldiniz Sayın"
    lawsuit_link_xpath = "//a[@href='http://themiscode.com/panel/Lawsuit/index']"

    # LawsuitPage elements

    # Find case files elements
    filter_case_state_dropbox_id = "inputState"
    filter_case_client_txtbox_name = "muvekkil"
    filter_file_no_txtbox_id = "foy-no"
    filter_defendant_txtbox_name = "karsi_taraf"
    filter_case_type_dropbox_name = "dava_turu"
    filter_search_btn_id = "ara-btn"
    filtered_search_result_sheet_no_xpath = "//a[contains(text(),'9000')]"
    clear_filter_btn_xpath = "//button[contains(@class,'temizle mr-2')]"
    filtered_table_first_row_xpath = "//table[@class='table table-striped']//tbody//tr//th[1]"
    back_error_message_css = "#main-message > h1"
    filtered_table_first_row_pre_xpath = '//*[@id="dava-dosyalari-goruntule"]/div/div[2]/div/pre[1]'




    # Case files elements
    case_table_xpath = '//*[@id="dava-dosyalari-goruntule"]/div/div[2]/div/table/tbody/tr'
    case_create_btn_id = "dosya-ekle-btn"
    case_type_dropbox_id = "dv_blg_turu"
    case_type_detail_dropbox_id = "dv_blg_turu_detay"
    case_subject_txtbox_id = "dv_blg_konu"
    case_city_dropbox_id = "dv_blg_il"
    case_city_region_txtbox_id = "dv_blg_ilce"
    case_create_date_time_picker_id = "dv_blg_acilis_tarihi"
    court_no_dropbox_id = "dv_blg_mahkeme_no"
    court_name_txtbox_id = "dv_blg_mahkeme_adi"
    case_status_dropbox_id = "dv_blg_dava_durumu"
    sheet_no_txtbox_id = "dv_blg_foy_no"
    case_value_txtbox_id = "dv_blg_dava_degeri"
    case_value_currency_dropbox_id = "dv_blg_dava_degeri_kur"
    case_extra_year_txtbox_id = "dv_blg_esas_yil_lbl"
    case_extra_no_txtbox_id = "dv_blg_esas_yil"
    case_decision_year_txtbox_id = "dv_blg_karar_yil_lbl"
    case_decision_year_no_txtbox_id = "dv_blg_karar_yil"
    case_decision_date_txtbox_id = "dv_blg_karar_tarih_tarih_lbl"
    case_decision_date_no_txtbox_id = "dv_blg_karar_tarih_tarih"
    case_final_date_txtbox_id = "dv_blg_kesinlesme_tarihi"
    case_add_btn_id = "dava-bilgi-ekle"

    # Lawsuit Person Information elements
    # Client information elements
    client_type_person_radio_css = "#muvekkil_wrapper > div > div:nth-child(1) > div:nth-child(2) > div > label > input"
    client_type_company_radio_css = "#muvekkil_wrapper > div > div:nth-child(1) > div:nth-child(3) > div > label > input"
    client_case_davali_radio_css = "#taraf-davali"
    client_case_davaci_radio_css = "#taraf-davaci"
    client_is_adult_radio_css = "#muvekkil_wrapper > div > div:nth-child(3) > div:nth-child(2) > div > label > input"
    client_is_not_adult_radio_css = "#muvekkil_wrapper > div > div:nth-child(3) > div:nth-child(3) > div > label > input"
    client_name_txtbox_name = "muvekkil_adi_soyadi"
    client_citizen_no_txtbox_name = "muvekkil_tc_kimlik_no"
    client_tel_no_txtbox_id = "muvekkil_telefon"
    client_address_txtarea_id = "muvekkil_adres"
    client_add_btn_id = "muvekkil-ekle"

    # Defendant information elements
    defendant_type_person_radio_css = "#detaylar > div > div:nth-child(4) > div > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div > label > input"
    defendant_type_company_radio_css = "#detaylar > div > div:nth-child(4) > div > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div > label > input"
    defendant_case_davali_radio_css = "#taraf-davali-2"
    defendant_case_davaci_radio_css = "#taraf-davaci-2"
    defendant_is_adult_radio_css = "#detaylar > div > div:nth-child(4) > div > div:nth-child(4) > div:nth-child(3) > div:nth-child(2) > div > label > input"
    defendant_is_not_adult_radio_css = "#detaylar > div > div:nth-child(4) > div > div:nth-child(4) > div:nth-child(3) > div:nth-child(3) > div > label > input"
    defendant_name_txtbox_name = "karsi_taraf_adi_soyadi"
    defendant_citizen_no_txtbox_name = "karsi_taraf_tc_kimlik_no"
    defendant_tel_no_txtbox_id = "karsi_taraf_telefon"
    defendant_address_txtarea_id = "karsi_taraf_adres"
    defendant_add_btn_id = "karsi-taraf-ekle"

    # Case details notes details
    case_details_notes_txtarea_name = "gorusme_notu"
    lawyer_dropbox_css = "#yetkili-avukat > div.form-group.row > div.col-10.col-md-5 > select"
    lawyer_add_btn_css = "#yetkili-avukat > div.form-group.row > div.col-2.col-md-1 > button"
    additional_lawyer_dropbox_css = "#yet_2 > div.col-10.col-md-5 > select"
    submit_btn_name = "kaydet"
    discard_btn_css = "#detaylar > div > div:nth-child(6) > div.d-flex > div.text-right > button.iptal.btn.border-0"

    # Edit case scenario elements
    # Table elements
    # Edit button
    # Commented out this xpath locator since it is not reliable. It can be changed by developers
    # table_last_row_xpath = '//*[@id="dava-dosyalari-goruntule"]/div/div[2]/div/table/tbody/tr[1]/td[6]/a[2]'
    table_last_row_xpath = "//a[contains(text(),'Law and Person interaction / Ali Pala -')]"
    case_edit_information_btn_xpath = '//*[@id="dava-bilgileri"]/div/table/tbody/tr[1]/td[6]/a[1]'
    case_information_update_btn_id = "dava-bilgi-guncelle"

    # Alerts
    # Successfully saved alert message
    success_saved_alert_message_css = "div.alert.alert-success"

    #Tabs
    expense_tab_id = "masraflar-tab"
    evidence_tab_id = "deliller-tab"











