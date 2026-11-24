import json

import pytest

from login import LoginPage

test_data_path = 'data/test_endToEndPractice.json'

with open(test_data_path) as file:
    test_data = json.load(file)
    test_list = test_data["data"]


@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):

    driver = browserInstance

    loginPage = LoginPage(driver)

    loginPage.getTitle()

    shop_page = loginPage.login_page(test_list_item["username"],test_list_item["password"])

    shop_page.add_product_to_card(test_list_item["productName"])

    shop_page.getTitle()

    checkout_confirmation = shop_page.go_to_card()

    checkout_confirmation.checkout()

    checkout_confirmation.enter_delivery_address("Azerbaijan")

    checkout_confirmation.validate_order()

