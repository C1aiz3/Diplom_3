import time

import allure
import pytest
from src.pages.main_page import MainPage
from src.pages.orders_feed_page import OrdersFeedPage
from src.locators.orders_feed_locators import OrdersFeedLocators as OFL
from src.locators.personal_account_page_locators import PersonalAccountPageLocators as PAPL
from src.locators.main_page_locators import MainPageLocators as MPL

class TestOrdersFeedPage():

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.step('Тест модального окна заказа в ленте заказов')
    def test_orders_feed_page_modal(self, driver):
        scooter_orders_feed_page = OrdersFeedPage(driver)
        scooter_orders_feed_page.open_url('feed')
        scooter_orders_feed_page.click_element(OFL.SOME_ORDER)
        assert scooter_orders_feed_page.find_element(OFL.ORDER_MODAL).is_displayed()


    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.step('Тест отображения заказа пользователя в ленте заказов')
    def test_user_order_in_orders_feed(self, driver):
        scooter_main_page = MainPage(driver)
        scooter_main_page.open_url('login')
        scooter_main_page.auth()
        scooter_main_page.drag_and_release_item(MPL.FLUORESCENT_BUN, MPL.DRAG_AND_DROP_FIELD)
        scooter_main_page.click_element(MPL.MAKE_ORDER_BUTTON)
        time.sleep(3)
        scooter_main_page.click_element(MPL.CLOSE_ORDER_MODAL)
        scooter_orders_feed_page = OrdersFeedPage(driver)
        scooter_orders_feed_page.click_element(PAPL.PERSONAL_ACCOUNT_BUTTON)
        scooter_orders_feed_page.click_element(PAPL.ORDER_HISTORY_BUTTON)
        last_number = scooter_orders_feed_page.get_last_list_elements_text(OFL.LAST_ORDER_NUMBER)
        scooter_orders_feed_page.click_element(MPL.ORDERS_FEED_BUTTON)
        actual_number = scooter_orders_feed_page.find_element(OFL.ACTUAL_ORDER_NUMBER).text
        assert actual_number == last_number

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.step('Тест изменения общего счетчика заказов после создания заказа')
    def test_change_total_counter_after_order(self, driver):
        scooter_main_page = MainPage(driver)
        scooter_main_page.open_url('login')
        scooter_main_page.auth()
        scooter_main_page.click_element(MPL.ORDERS_FEED_BUTTON)
        scooter_orders_feed_page = OrdersFeedPage(driver)
        total_old = scooter_orders_feed_page.find_element(OFL.TOTAL_ORDERS_COUNTER).text
        scooter_orders_feed_page.click_element(MPL.CONSTRUCTOR_BUTTON)
        scooter_main_page.drag_and_release_item(MPL.FLUORESCENT_BUN, MPL.DRAG_AND_DROP_FIELD)
        scooter_main_page.click_element(MPL.MAKE_ORDER_BUTTON)
        time.sleep(3)
        scooter_main_page.click_element(MPL.CLOSE_ORDER_MODAL)
        scooter_main_page.click_element(MPL.ORDERS_FEED_BUTTON)
        total_new = scooter_orders_feed_page.find_element(OFL.TOTAL_ORDERS_COUNTER).text
        assert total_old < total_new #все также падает для firefox

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.step('Тест изменения счетчика заказов за сегодня после создания заказа')
    def test_change_today_counter_after_order(self, driver):
        scooter_main_page = MainPage(driver)
        scooter_main_page.open_url('login')
        scooter_main_page.auth()
        scooter_main_page.click_element(MPL.ORDERS_FEED_BUTTON)
        scooter_orders_feed_page = OrdersFeedPage(driver)
        total_old = scooter_orders_feed_page.find_element(OFL.TODAY_ORDERS_COUNTER).text
        scooter_orders_feed_page.click_element(MPL.CONSTRUCTOR_BUTTON)
        scooter_main_page.drag_and_release_item(MPL.FLUORESCENT_BUN, MPL.DRAG_AND_DROP_FIELD)
        scooter_main_page.click_element(MPL.MAKE_ORDER_BUTTON)
        time.sleep(3)
        scooter_main_page.click_element(MPL.CLOSE_ORDER_MODAL)
        scooter_main_page.click_element(MPL.ORDERS_FEED_BUTTON)
        total_new = scooter_orders_feed_page.find_element(OFL.TODAY_ORDERS_COUNTER).text
        assert total_old < total_new  # все также падает для firefox

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.step('Тест отображения номера заказа в работе')
    def test_order_number_in_work(self, driver):
        scooter_main_page = MainPage(driver)
        scooter_main_page.open_url('login')
        scooter_main_page.auth()
        scooter_main_page.drag_and_release_item(MPL.FLUORESCENT_BUN, MPL.DRAG_AND_DROP_FIELD)
        scooter_main_page.click_element(MPL.MAKE_ORDER_BUTTON)
        time.sleep(3)
        number = scooter_main_page.find_element(OFL.ORDER_NUMBER_MODAL).text
        scooter_main_page.click_element(MPL.CLOSE_ORDER_MODAL)
        scooter_main_page.click_element(MPL.ORDERS_FEED_BUTTON)
        scooter_orders_feed_page = OrdersFeedPage(driver)
        in_progress_orders = scooter_orders_feed_page.find_element(OFL.IN_PROGRESS_SECTION).text
        assert number in in_progress_orders