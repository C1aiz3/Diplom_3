import allure
from src.helpers import FakeData as FD
from src.pages.base_page import BasePage
from src.locators.pass_recovery_page_locators import PassRecoveryPageLocators as PRPL



class PassRecoveryPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполнение полей')
    def fill_the_field(self):
        with allure.step(f'Fill the field'):
            field = self.find_element(PRPL.EMAIL_FIELD_Recovery_PAGE)
            field.send_keys(FD.f_mail())

    @allure.step('Нажатие на отображение пароля и проверка появления текста')
    def click_and_check_hide_pass_button(self):
        self.click_element(PRPL.SHOW_HIDE_PASS_BUTTON)
        return self.find_element(PRPL.PASS_FIELD).get_attribute('type')

    @allure.step('Переход на страницу авторизации и нажатие на кнопку забыли пароль')
    def go_to_login_page_and_press_forgot_button(self):
        self.open_url('login')
        self.click_element(PRPL.AUTH_FORGOT_PASS_BUTTON)

    @allure.step('Нажатие на восстановить пароль и проверка изменения URL')
    def press_reset_and_wait_url_changes(self):
        self.click_element(PRPL.RECOVERY_FORGOT_PASS_BUTTON)
        self.wait_until_url_changes()