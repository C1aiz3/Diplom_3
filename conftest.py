import pytest
from browser_factory import BrowserFactory


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    driver = BrowserFactory.get_driver(browser)
    yield driver
    driver.quit()

