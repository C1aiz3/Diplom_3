import allure
import pytest
from src.pages.main_page import MainPage
from src.pages.orders_feed_page import OrdersFeedPage
from src.pages.personal_account_page import PersonalAccountPage


class TestOrdersFeedPage():

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест модального окна заказа в ленте заказов')
    def test_orders_feed_page_modal(self, driver):
        burger_orders_feed_page = OrdersFeedPage(driver)
        burger_orders_feed_page.open_url('feed')
        assert burger_orders_feed_page.click_some_order_and_get_modal()


    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест отображения заказа пользователя в ленте заказов')
    def test_user_order_in_orders_feed(self, driver):
        burger_personal_account_page = PersonalAccountPage(driver)
        burger_personal_account_page.auth()
        burger_main_page = MainPage(driver)
        burger_main_page.make_order()
        burger_orders_feed_page = OrdersFeedPage(driver)
        expected = burger_orders_feed_page.escape_imitation_and_get_order_number()
        burger_personal_account_page.go_to_order_history_in_profile()
        burger_orders_feed_page.order_number_presence('LAST', expected)
        last_number = burger_orders_feed_page.get_last_list_elements_text()
        burger_main_page.click_orders_feed_button()
        burger_orders_feed_page.order_number_presence('ACTUAL', expected)
        actual_number = burger_orders_feed_page.get_order_text()
        assert last_number == actual_number

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест изменения общего счетчика заказов после создания заказа')
    def test_change_total_counter_after_order(self, driver):
        burger_personal_account_page = PersonalAccountPage(driver)
        burger_personal_account_page.auth()
        burger_main_page = MainPage(driver)
        burger_main_page.click_orders_feed_button()
        burger_orders_feed_page = OrdersFeedPage(driver)
        total_old = burger_orders_feed_page.get_counters_in_orders_feed('TOTAL')
        burger_main_page.click_constructor_button()
        burger_main_page.make_order()
        burger_orders_feed_page.escape_imitation()
        burger_main_page.click_orders_feed_button()
        burger_main_page.wait_two_sec()
        total_new = burger_orders_feed_page.get_counters_in_orders_feed('TOTAL')
        assert total_old < total_new #все также падает для firefox

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест изменения счетчика заказов за сегодня после создания заказа')
    def test_change_today_counter_after_order(self, driver):
        burger_personal_account_page = PersonalAccountPage(driver)
        burger_personal_account_page.auth()
        burger_main_page = MainPage(driver)
        burger_main_page.click_orders_feed_button()
        burger_orders_feed_page = OrdersFeedPage(driver)
        today_old = burger_orders_feed_page.get_counters_in_orders_feed('TODAY')
        burger_main_page.click_constructor_button()
        burger_main_page.make_order()
        burger_orders_feed_page.escape_imitation()
        burger_main_page.click_orders_feed_button()
        burger_main_page.wait_two_sec()
        today_new = burger_orders_feed_page.get_counters_in_orders_feed('TODAY')
        assert today_old < today_new  # все также падает для firefox

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест отображения номера заказа в работе')
    def test_order_number_in_work(self, driver):
        burger_personal_account_page = PersonalAccountPage(driver)
        burger_personal_account_page.auth()
        burger_main_page = MainPage(driver)
        burger_main_page.make_order()
        burger_orders_feed_page = OrdersFeedPage(driver)
        burger_orders_feed_page.escape_imitation()
        number = burger_orders_feed_page.escape_imitation_and_get_order_number()
        burger_main_page.click_orders_feed_button()
        burger_orders_feed_page.wait_two_sec()
        in_progress_orders = burger_orders_feed_page.get_order_number_in_progress()
        assert f'0{number}' in in_progress_orders