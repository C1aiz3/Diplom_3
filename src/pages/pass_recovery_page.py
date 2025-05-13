import allure
from src.pages.base_page import BasePage



class PassRecoveryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def fill_the_field(self, locator, data):
        with allure.step(f'Fill the field'):
            field = self.find_element(locator)
            field.send_keys(data)