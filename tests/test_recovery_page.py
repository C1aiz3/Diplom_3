import time

import allure
import pytest
from src.data import URLS
from src.pages.pass_recovery_page import PassRecoveryPage

from src.helpers import FakeData as FD


class TestPassRecoveryPage():

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_navigate_to_recovery_page(self, driver):
        scooter_login_page = PassRecoveryPage(driver)
        scooter_login_page.go_to_login_page_and_press_forgot_button()
        assert scooter_login_page.current_url() == URLS.FORGOT_PASSWORD_URL

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Проверка ввода почты и восстановления пароля')
    def test_email_input_and_recovery(self, driver):
        scooter_login_page = PassRecoveryPage(driver)
        scooter_login_page.go_to_login_page_and_press_forgot_button()
        scooter_login_page.fill_the_field()
        scooter_login_page.press_reset_and_wait_url_changes()
        assert scooter_login_page.current_url() == URLS.RESET_PASSWORD_URL

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Проверка функционала показать/скрыть пароль')
    def test_show_hide_password(self, driver):
        scooter_login_page = PassRecoveryPage(driver)
        scooter_login_page.go_to_login_page_and_press_forgot_button()
        scooter_login_page.fill_the_field()
        scooter_login_page.press_reset_and_wait_url_changes()
        assert 'text' in scooter_login_page.click_and_check_hide_pass_button()