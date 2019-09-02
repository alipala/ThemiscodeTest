import pytest
from selenium import webdriver


class Base:

    @pytest.fixture(autouse=True)
    def set_up(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome(executable_path="D:/_python/themis/Drivers/chromedriver.exe")
        print("-----------------------------------------")
        print("Test started")
        self.driver.implicitly_wait(10)
        self.driver.get("http://themiscode.com/panel/login.html")
        self.driver.maximize_window()

        yield self.driver
        if self.driver is not None:
            print("-----------------------------------------")
            print("Tests finished")
            self.driver.close()
            self.driver.quit()



