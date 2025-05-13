import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.data import URL
import time
from src.data import EMAIL, PASSWORD
from src.locators.personal_account_page_locators import PersonalAccountPageLocators as PAPL
from src.locators.orders_feed_locators import OrdersFeedLocators as OFL


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.site = URL

    @allure.step('Открытие страницы')
    def open_url(self, added_data = ''):
        self.driver.get(f'{self.site}{added_data}')

    @allure.step('Поиск элемента')
    def find_element(self, *locator, time = 5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(*locator))

    @allure.step('Клик по элементу')
    def click_element(self, *locator, time=5):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(*locator)).click()

    @allure.step('Авторизация')
    def auth(self):
        self.find_element(PAPL.EMAIL_FIELD).send_keys(EMAIL)
        self.find_element(PAPL.PASSWORD_FIELD).send_keys(PASSWORD)
        time.sleep(1)
        self.find_element(PAPL.ENTER_BUTTON).click()
        time.sleep(1)

    @allure.step('Получение текста последнего элемента из списка')
    def get_last_list_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        last_element = elements[-1]
        text_element = last_element.find_element(*OFL.LAST_ORDER_NUMBER)
        return text_element.text
