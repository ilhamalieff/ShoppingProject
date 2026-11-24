
from selenium import webdriver


from selenium.webdriver.chrome.options import Options
from login import LoginPage

options = Options()
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False,
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-features=PasswordLeakDetection")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(4)

driver.get("https://rahulshettyacademy.com/loginpagePractise/")

loginPage = LoginPage(driver)

shop_page = loginPage.login_page()

shop_page.add_product_to_card("Blackberry")

checkout_confirmation =shop_page.go_to_card()

checkout_confirmation.checkout()

checkout_confirmation.enter_delivery_address("Azerbaijan")

checkout_confirmation.validate_order()


























