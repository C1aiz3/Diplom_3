import allure
from src.pages.base_page import BasePage
from selenium.webdriver import ActionChains
from src.locators.main_page_locators import MainPageLocators as MPL





class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Перетаскивание элемента')
    def drag_and_release_bun(self):
        with allure.step(f'Drag from {MPL.FLUORESCENT_BUN} to {MPL.DRAG_AND_DROP_FIELD} and release'):
            start = self.find_element(MPL.FLUORESCENT_BUN)
            finish = self.find_element(MPL.DRAG_AND_DROP_FIELD)

            actions = ActionChains(self.driver)
            actions.click_and_hold(start)
            actions.move_to_element(finish)
            actions.release(finish)
            actions.perform()

    @allure.step('Нажатие кнопки Конструктор')
    def click_constructor_button(self):
        self.click_element(MPL.CONSTRUCTOR_BUTTON)

    @allure.step('Нажатие кнопки История заказов')
    def click_orders_feed_button(self):
        self.click_element(MPL.ORDERS_FEED_BUTTON)

    @allure.step('Нажатие на булку')
    def click_on_bun(self):
        self.click_element(MPL.FLUORESCENT_BUN)

    @allure.step('Отображение модальных окон')
    def modal_displayed(self, locator):
        if locator == 'INGREDIENT':
            return self.find_element(MPL.INGREDIENT_MODAL).is_displayed()
        elif locator == 'ORDER':
            return self.find_element(MPL.ORDER_MODAL).is_displayed()

    @allure.step('Закрытие модального окна ингредиента')
    def close_ing_modal(self):
        self.click_element(MPL.INGREDIENT_MODAL_CLOSE)

    @allure.step('Проверка на закрытие модального окна ингредиента')
    def ing_modal_disappear(self):
        return self.wait_element_disappear(MPL.INGREDIENT_MODAL)

    @allure.step('Счетчик ингредиентов')
    def ing_counter_text(self):
        return self.find_element(MPL.INGREDIENT_COUNTER).text

    @allure.step('Оформление заказа')
    def make_order(self):
        self.drag_and_release_bun()
        self.click_element(MPL.MAKE_ORDER_BUTTON)







