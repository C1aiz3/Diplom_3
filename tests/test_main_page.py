import time
import pytest
import allure
from src.pages.main_page import MainPage
from src.locators.main_page_locators import MainPageLocators as MPL



class TestMainPage():

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.step('Тест-сценарий функциональности главной страницы')
    def test_main_page_functional(self, driver):
        scooter_main_page = MainPage(driver)
        scooter_main_page.open_url('login')
        time.sleep(2)
        scooter_main_page.click_element(MPL.ORDERS_FEED_BUTTON)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/feed'
        scooter_main_page.click_element(MPL.CONSTRUCTOR_BUTTON)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        scooter_main_page.click_element(MPL.FLUORESCENT_BUN)
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/ingredient/61c0c5a71d1f82001bdaaa6d'
        scooter_main_page.click_element(MPL.INGREDIENT_MODAL_CLOSE)
        scooter_main_page.drag_and_release_item(MPL.FLUORESCENT_BUN, MPL.DRAG_AND_DROP_FIELD)
        assert scooter_main_page.find_element(MPL.INGREDIENT_COUNTER).text == '2' #на firefox падает, хотя chrome отрабатывает

    @pytest.mark.parametrize("driver", ["chrome"], indirect=True)
    @allure.step('Тест-сценарий статуса авторизации при создании заказа')
    def test_make_order_auth_status(self, driver):
        scooter_main_page = MainPage(driver)
        scooter_main_page.open_url('login')
        scooter_main_page.auth()
        scooter_main_page.drag_and_release_item(MPL.FLUORESCENT_BUN, MPL.DRAG_AND_DROP_FIELD)
        scooter_main_page.click_element(MPL.MAKE_ORDER_BUTTON)
        assert scooter_main_page.find_element(MPL.ORDER_MODAL).is_displayed()
