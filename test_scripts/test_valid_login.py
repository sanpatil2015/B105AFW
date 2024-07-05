from generic.base_class import BaseClass
from generic.utility import Excel
from page.login_page import LoginPage
from page.home_page import HomePage
class Test_ValidLogin(BaseClass):

    def test_validlogin(self):
        #read data
            un = Excel.get_data(self.XLPATH, 'ValidLogin', 2, 1)
            pw = Excel.get_data(self.XLPATH, 'ValidLogin', 2, 2)

        # 1. enter valid username
            login_page=LoginPage(self.driver)
            login_page.set_username(un)

        # 2. enter valid password
            login_page.set_password(pw)

        # 3. click on go button
            login_page.click_go()

        # 4. verify home page is displayed
            home_page=HomePage(self.driver)
            result=home_page.verify_homepage_is_displayed(self.wait)
            assert result
