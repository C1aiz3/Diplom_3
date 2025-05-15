import pytest
import allure
from src.pages.main_page import MainPage
from src.data import URLS
from src.pages.personal_account_page import PersonalAccountPage


class TestMainPage:
    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест перехода в конструктор')
    def test_constructor_navigation(self, driver):
        burger_main_page = MainPage(driver)
        burger_main_page.open_url()
        burger_main_page.click_constructor_button()
        assert burger_main_page.current_url() == URLS.MAIN_PAGE_URL

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест перехода в ленту заказов')
    def test_orders_feed_navigation(self, driver):
        burger_main_page = MainPage(driver)
        burger_main_page.open_url()
        burger_main_page.click_orders_feed_button()
        assert burger_main_page.current_url() == URLS.FEED_PAGE_URL

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест открытия модального окна с деталями ингредиента')
    def test_ingredient_details_modal(self, driver):
        burger_main_page = MainPage(driver)
        burger_main_page.open_url()
        burger_main_page.click_on_bun()
        assert burger_main_page.current_url() == URLS.INGREDIENT_URL
        assert burger_main_page.modal_displayed('INGREDIENT')

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест закрытия модального окна с деталями ингредиента')
    def test_close_ingredient_modal(self, driver):
        burger_main_page = MainPage(driver)
        burger_main_page.open_url()
        burger_main_page.click_on_bun()
        burger_main_page.close_ing_modal()
        assert burger_main_page.ing_modal_disappear()

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест увеличения счетчика ингредиента')
    def test_ingredient_counter_increase(self, driver):
        burger_main_page = MainPage(driver)
        burger_main_page.open_url()
        burger_main_page.drag_and_release_bun()
        assert burger_main_page.ing_counter_text() == '2'

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.step('Тест возможности оформить заказ авторизованному пользователю')
    def test_make_order_auth_status(self, driver):
        burger_personal_account_page = PersonalAccountPage(driver)
        burger_personal_account_page.auth()
        burger_main_page = MainPage(driver)
        burger_main_page.make_order()
        assert burger_main_page.modal_displayed('ORDER')