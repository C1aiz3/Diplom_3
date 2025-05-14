import pytest
import allure
from src.data import URLS
from src.pages.personal_account_page import PersonalAccountPage


class TestPersonalAccountPage:
    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест перехода в личный кабинет')
    def test_personal_account_button(self, driver):
        scooter_personal_account_page = PersonalAccountPage(driver)
        scooter_personal_account_page.go_to_profile()
        scooter_personal_account_page.wait_until_url_changes()
        assert scooter_personal_account_page.current_url() == URLS.PROFILE_PAGE_URL

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест перехода в историю заказов')
    def test_order_history_button(self, driver):
        scooter_personal_account_page = PersonalAccountPage(driver)
        scooter_personal_account_page.go_to_profile()
        scooter_personal_account_page.click_oder_history_button()
        assert scooter_personal_account_page.current_url() == URLS.ORDER_HISTORY_URL

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест выхода из аккаунта')
    def test_exit_button(self, driver):
        scooter_personal_account_page = PersonalAccountPage(driver)
        scooter_personal_account_page.go_to_profile()
        scooter_personal_account_page.click_exit_button()
        scooter_personal_account_page.wait_until_url_changes()
        assert scooter_personal_account_page.current_url() == URLS.LOGIN_PAGE_URL