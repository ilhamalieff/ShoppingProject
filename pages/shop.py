from selenium.webdriver.common.by import By
from pages.checkout_confirmation import CheckoutConfirmation
from utils.browserUtils import BrowserUtils

class Shop(BrowserUtils) :
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.shopLink = (By.CSS_SELECTOR, " a[href*='shop']")
        self.productCards = (By.XPATH, "//div[@class='card h-100']")
        self.checkOutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def add_product_to_card(self,productName):
        self.driver.find_element(*self.shopLink).click()

        products = self.driver.find_elements(*self.productCards)

        for product in products:

            product_name = product.find_element(By.XPATH, "div/h4/a").text

            if product_name == productName:
                product.find_element(By.XPATH, "div/button").click()

    def go_to_card(self):
        self.driver.find_element(*self.checkOutButton).click()

        checkout_confirmation = CheckoutConfirmation(self.driver)

        return checkout_confirmation
