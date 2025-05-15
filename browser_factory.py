from selenium import webdriver

class BrowserFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name == "chrome":
            return webdriver.Chrome()
        elif browser_name == "firefox":
            return webdriver.Firefox()
