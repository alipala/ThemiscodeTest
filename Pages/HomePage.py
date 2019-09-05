from Locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.logout_link_xpath = Locators.logout_link_xpath
        self.user_partial_link_text = Locators.user_partial_link_text
        self.lawsuit_link_xpath = Locators.lawsuit_link_xpath

    def click_law_suit_page(self):
        self.driver.find_element_by_xpath(self.lawsuit_link_xpath).click()

    def click_welcome_user_link(self):
        self.driver.find_element_by_partial_link_text(self.user_partial_link_text).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()


