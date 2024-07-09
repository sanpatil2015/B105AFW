from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.__logout = (By.XPATH, "//a[text()='Logout']")

    def verify_homepage_is_displayed(self, wait):
        try:
            wait.until(EC.visibility_of_element_located(self.__logout))
            print('Home Page is displayed')
            return True
        except:
            print('Home Page is NOT displayed')
            return False
