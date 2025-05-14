import allure
import pytest
from src.pages.main_page import MainPage
from src.pages.orders_feed_page import OrdersFeedPage




class TestOrdersFeedPage():

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест модального окна заказа в ленте заказов')
    def test_orders_feed_page_modal(self, driver):
        scooter_orders_feed_page = OrdersFeedPage(driver)
        scooter_orders_feed_page.open_url('feed')
        assert scooter_orders_feed_page.click_some_order_and_get_modal()


    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест отображения заказа пользователя в ленте заказов')
    def test_user_order_in_orders_feed(self, driver):
        scooter_main_page = MainPage(driver)
        scooter_main_page.open_url('login')
        scooter_main_page.auth()
        scooter_main_page.make_order()
        scooter_orders_feed_page = OrdersFeedPage(driver)
        expected = scooter_orders_feed_page.escape_imitation_and_get_order_number()
        scooter_orders_feed_page.go_to_order_history_in_profile()
        scooter_orders_feed_page.order_number_presence('LAST', expected)
        last_number = scooter_orders_feed_page.get_last_list_elements_text()
        scooter_main_page.click_orders_feed_button()
        scooter_orders_feed_page.order_number_presence('ACTUAL', expected)
        actual_number = scooter_orders_feed_page.get_order_text()
        assert last_number == actual_number

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест изменения общего счетчика заказов после создания заказа')
    def test_change_total_counter_after_order(self, driver):
        scooter_main_page = MainPage(driver)
        scooter_main_page.open_url('login')
        scooter_main_page.auth()
        scooter_main_page.click_orders_feed_button()
        scooter_orders_feed_page = OrdersFeedPage(driver)
        total_old = scooter_orders_feed_page.get_counters_in_orders_feed('TOTAL')
        scooter_main_page.click_constructor_button()
        scooter_main_page.make_order()
        scooter_orders_feed_page.escape_imitation()
        scooter_main_page.click_orders_feed_button()
        scooter_main_page.wait_two_sec()
        total_new = scooter_orders_feed_page.get_counters_in_orders_feed('TOTAL')
        assert total_old < total_new #все также падает для firefox

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест изменения счетчика заказов за сегодня после создания заказа')
    def test_change_today_counter_after_order(self, driver):
        scooter_main_page = MainPage(driver)
        scooter_main_page.open_url('login')
        scooter_main_page.auth()
        scooter_main_page.click_orders_feed_button()
        scooter_orders_feed_page = OrdersFeedPage(driver)
        today_old = scooter_orders_feed_page.get_counters_in_orders_feed('TODAY')
        scooter_main_page.click_constructor_button()
        scooter_main_page.make_order()
        scooter_orders_feed_page.escape_imitation()
        scooter_main_page.click_orders_feed_button()
        scooter_main_page.wait_two_sec()
        today_new = scooter_orders_feed_page.get_counters_in_orders_feed('TODAY')
        assert today_old < today_new  # все также падает для firefox

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.title('Тест отображения номера заказа в работе')
    def test_order_number_in_work(self, driver):
        scooter_main_page = MainPage(driver)
        scooter_main_page.open_url('login')
        scooter_main_page.auth()
        scooter_main_page.make_order()
        scooter_main_page.escape_imitation()
        scooter_orders_feed_page = OrdersFeedPage(driver)
        number = scooter_orders_feed_page.escape_imitation_and_get_order_number()
        scooter_main_page.click_orders_feed_button()
        scooter_orders_feed_page.wait_two_sec()
        in_progress_orders = scooter_orders_feed_page.get_order_number_in_progress()
        assert f'0{number}' in in_progress_orders