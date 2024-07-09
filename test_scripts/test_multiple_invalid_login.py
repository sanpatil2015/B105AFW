from generic.base_class import BaseClass
from generic.utility import Excel
from page.login_page import LoginPage
import pytest

class Test_InvalidLogin(BaseClass):

    @pytest.mark.run(order=3)
    def test_invalid_login(self):
        rc = Excel.get_rowcount(self.XLPATH, 'MultipleInvalidLogin')
        for i in range(2,rc+1):
            un = Excel.get_data(self.XLPATH, 'MultipleInvalidLogin', i, 1)
            pw = Excel.get_data(self.XLPATH, 'MultipleInvalidLogin', i, 2)

            # 1. enter invalid username
            login_page = LoginPage(self.driver)
            login_page.set_username(un)

            # 2. enter invalid password
            login_page.set_password(pw)

            # 3. click on go button
            login_page.click_go()

            # 4. verify error msg is displayed
            result=login_page.verify_errmsg_is_displayed(self.wait)
            assert result
