import time
import pytest
import allure
from src.pages.personal_account_page import PersonalAccountPage
from src.locators.personal_account_page_locators import PersonalAccountPageLocators as PAPL


class TestPersonalAccountPage():

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.step('Тест-сценарий страницы личного кабинета')
    def test_personal_account_page(self, driver):
        scooter_personal_account_page = PersonalAccountPage(driver)
        scooter_personal_account_page.open_url('login')
        scooter_personal_account_page.auth()
        scooter_personal_account_page.click_element(PAPL.PERSONAL_ACCOUNT_BUTTON)
        time.sleep(2)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
        scooter_personal_account_page.click_element(PAPL.ORDER_HISTORY_BUTTON)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/order-history'
        scooter_personal_account_page.click_element(PAPL.EXIT_BUTTON)
        time.sleep(2)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'