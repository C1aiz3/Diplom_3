import allure
import time
from src.data import URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.site = URL

    @allure.step('Открытие страницы')
    def open_url(self, added_data = ''):
        self.driver.get(f'{self.site}{added_data}')

    @allure.step('Поиск элемента')
    def find_element(self, locator, time = 5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Получение текущего URL')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание изменения URL')
    def wait_until_url_changes(self, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_changes(self.driver.current_url))

    @allure.step('Ожидание 2 секунды')
    def wait_two_sec(self):
        time.sleep(2)

    @allure.step('Ожидание исчезновения элемента')
    def wait_element_disappear(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located((locator)))

    @allure.step('Ожидание необходимого текста в элементе')
    def text_in_element_presence(self, locator, text, time=10):
        WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element((locator), text))