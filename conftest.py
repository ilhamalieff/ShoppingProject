import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        choices=["chrome", "microsoft_edge"],
        help="browser selection",
    )


def apply_common_options(options):
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
    return options


@pytest.fixture(scope="function")
def browserInstance(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome(options=apply_common_options(ChromeOptions()),)
    elif browser_name == "microsoft_edge":
        driver = webdriver.Edge(options=apply_common_options(EdgeOptions()))
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.implicitly_wait(4)
    yield driver
    driver.quit()

@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin( 'html' )
    outcome = yield
    report = outcome.get_result()
    extra = getattr( report, 'extra', [] )

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr( report, 'wasxfail' )
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join( os.path.dirname( __file__ ), 'reports' )
            file_name = os.path.join( reports_dir, report.nodeid.replace( "::", "_" ) + ".png" )
            print( "file name is " + file_name )
            _capture_screenshot( file_name )
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append( pytest_html.extras.html( html ) )
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)