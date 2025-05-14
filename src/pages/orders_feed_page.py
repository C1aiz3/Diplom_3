import allure
from selenium.webdriver import ActionChains, Keys
from src.pages.base_page import BasePage
from src.locators.orders_feed_locators import OrdersFeedLocators as OFL
from src.locators.personal_account_page_locators import PersonalAccountPageLocators as PAPL




class OrdersFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получение текста последнего элемента списка')
    def get_last_list_elements_text(self):
        return self.find_element(OFL.LAST_ORDER_NUMBER).text

    @allure.step('Открытие модального окна заказа')
    def click_some_order_and_get_modal(self):
        self.click_element(OFL.SOME_ORDER)
        return self.find_element(OFL.ORDER_MODAL).is_displayed()

    @allure.step('История заказов в профиле')
    def go_to_order_history_in_profile(self):
        self.click_element(PAPL.PERSONAL_ACCOUNT_BUTTON)
        self.click_element(PAPL.ORDER_HISTORY_BUTTON)

    @allure.step('Получение текста последнего заказа в ленте заказов')
    def get_order_text(self):
        return self.find_element(OFL.ACTUAL_ORDER_NUMBER).text

    @allure.step('Получение значений счетчиков заказов')
    def get_counters_in_orders_feed(self, locator):
        if locator == 'TOTAL':
            return self.find_element(OFL.TOTAL_ORDERS_COUNTER).text
        if locator == 'TODAY':
            return self.find_element(OFL.TODAY_ORDERS_COUNTER).text

    @allure.step('Имитация кнопки ESC и забор номера заказа из модального окна заказа')
    def escape_imitation_and_get_order_number(self):
        number = self.find_element(OFL.ORDER_NUMBER_MODAL).text
        with allure.step(f'ESC button imitation'):
            try:
                ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            except:
                pass
            return number

    @allure.step('Получение номера заказа в работе')
    def get_order_number_in_progress(self):
        return self.find_element(OFL.IN_PROGRESS_SECTION).text

    @allure.step('Ожидание отображения номера заказа на сайте')
    def order_number_presence(self, locator, text):
        if locator == 'LAST':
            return self.text_in_element_presence(OFL.LAST_ORDER_NUMBER, text)
        elif locator == 'ACTUAL':
            return self.text_in_element_presence(OFL.ACTUAL_ORDER_NUMBER, text)










