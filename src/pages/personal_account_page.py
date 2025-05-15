import allure
from src.data import EMAIL, PASSWORD
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

    @allure.step('История заказов в профиле')
    def go_to_order_history_in_profile(self):
        self.click_element(PAPL.PERSONAL_ACCOUNT_BUTTON)
        self.click_element(PAPL.ORDER_HISTORY_BUTTON)

    @allure.step('Авторизация')
    def auth(self):
        self.open_url('login')
        self.find_element(PAPL.EMAIL_FIELD).send_keys(EMAIL)
        self.find_element(PAPL.PASSWORD_FIELD).send_keys(PASSWORD)
        self.find_element(PAPL.ENTER_BUTTON).click()
