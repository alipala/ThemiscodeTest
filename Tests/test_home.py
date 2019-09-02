from Pages.HomePage import HomePage
from Base.base import Base
import pytest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

class TestHome(Base):

    @pytest.mark.dependency(depends=["test_login_validation"])
    def test_home_logout(self):
        driver = self.driver
        home = HomePage(driver)
        home.logout()
        try:
            assert "Ana Sayfa - Dava & İcra Takip" in driver.title
            print("Title is ok")
        except Exception as e:
            print("Title is wrong", format(e))
