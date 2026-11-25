from selenium.webdriver.common.by import By
from pages.shop import Shop
from utils.browserUtils import BrowserUtils

class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.ID, "password")
        self.acceptTerms = (By.CSS_SELECTOR, "#terms")
        self.signInButton = (By.ID, "signInBtn")

    def login_page(self,username,password):
        self.driver.find_element(*self.username).send_keys(username)

        self.driver.find_element(*self.password).send_keys(password)

        self.driver.find_element(*self.acceptTerms).click()

        self.driver.find_element(*self.signInButton).click()

        shop_page = Shop(self.driver)

        return shop_page