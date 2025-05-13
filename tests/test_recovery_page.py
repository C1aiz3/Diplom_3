import time
import allure
import pytest
from src.pages.pass_recovery_page import PassRecoveryPage
from src.locators.pass_recovery_page_locators import PassRecoveryPageLocators as PRPL
from src.data import FakeData as FD


class TestPassRecoveryPage():

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    def test_pass_recovery_page(self, driver):
        scooter_login_page = PassRecoveryPage(driver)

        with allure.step(f'Тест-сценарий страницы восстановление пароля'):
            scooter_login_page.open_url('login')
            time.sleep(2)
            scooter_login_page.click_element(PRPL.AUTH_FORGOT_PASS_BUTTON)
            assert driver.current_url == 'https://stellarburgers.nomoreparties.site/forgot-password'
            scooter_login_page.fill_the_field(PRPL.EMAIL_FIELD_Recovery_PAGE, FD.f_mail())
            scooter_login_page.click_element(PRPL.RECOVERY_FORGOT_PASS_BUTTON)
            time.sleep(2)
            assert driver.current_url == 'https://stellarburgers.nomoreparties.site/reset-password'
            scooter_login_page.click_element(PRPL.SHOW_HIDE_PASS_BUTTON)
            assert 'text' in scooter_login_page.find_element(PRPL.PASS_FIELD).get_attribute('type')