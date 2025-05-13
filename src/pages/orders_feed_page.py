import allure
from src.pages.base_page import BasePage
from selenium.webdriver.common.by import By





class OrdersFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получение текста последнего элемента списка')
    def get_last_list_elements_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Проверка отображения заказа в ленте заказов')
    def order_feed_displayed(self, number):
        order_locator = (By.XPATH, f'//p[contains(@class, "OrderFeed_number") and text()="{number}"]')
        return self.element_displayed(order_locator)
