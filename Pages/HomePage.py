from Locators.locators import Locators


class HomePage:

    def _init__(self, driver):
        self.driver = driver
        self.logout_link_xpath = Locators.logout_link_xpath

    def logout(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()

