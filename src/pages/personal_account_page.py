import allure
from src.pages.base_page import BasePage
from src.locators.personal_account_page_locators import PersonalAccountPageLocators as PAPL




class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход в профиль')
    def go_to_profile(self):
        self.open_url('login')
        self.auth()
        self.click_element(PAPL.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Нажатие на кнопку история заказов')
    def click_oder_history_button(self):
        self.click_element(PAPL.ORDER_HISTORY_BUTTON)

    @allure.step('Нажатие на кнопку выйти')
    def click_exit_button(self):
        self.click_element(PAPL.EXIT_BUTTON)
