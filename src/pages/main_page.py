
import allure
from src.pages.base_page import BasePage
from selenium.webdriver import ActionChains




class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def drag_and_release_item(self, start_position, finish_position):
        with allure.step(f'Drag from {start_position} to {finish_position} and release'):
            start = self.find_element(start_position)
            finish = self.find_element(finish_position)

            actions = ActionChains(self.driver)
            actions.click_and_hold(start)
            actions.move_to_element(finish)
            actions.release(finish)
            actions.perform()



