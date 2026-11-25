# Selenium + PyTest Practice Project

End-to-end UI test automation practice built while learning
Python, Selenium WebDriver and PyTest. The tests run against
the demo site https://rahulshettyacademy.com/loginpagePractise/.

> Note: this is a course practice project. My independent
> portfolio projects will be linked below once they are ready.

## What it covers

- Page Object Model (login, shop, checkout pages)
- PyTest fixtures and `conftest.py` (browser setup/teardown)
- Data-driven tests with `parametrize` and a JSON file
- Cross-browser option: Chrome and Microsoft Edge
- Automatic screenshot on test failure, HTML report

## Tech stack

Python 3, Selenium WebDriver, PyTest, pytest-html

## Project structure

    ├── data/          # test data (JSON)
    ├── utils/         # shared helper classes
    ├── login.py       # login page object
    ├── shop.py        # shop page object
    ├── checkout_confirmation.py
    ├── conftest.py    # fixtures, CLI options, screenshots
    └── test_endToEndPractice.py

## How to run

1. Install dependencies: `pip install -r requirements.txt`
2. Run all tests: `pytest`
3. Run in Edge: `pytest --browser_name=microsoft_edge`
4. HTML report: `pytest --html=reports/report.html`

## Test scenario

Log in, add a product to the cart, go to checkout, choose a
delivery country, confirm the order and verify the success message.

## Author

Ilham Aliyev