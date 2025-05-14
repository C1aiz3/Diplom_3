import allure
import time

from selenium.webdriver import ActionChains, Keys

from src.data import URL
from src.data import EMAIL, PASSWORD
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    def find_element(self, locator, time = 5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Авторизация')
    def auth(self):
        self.find_element(PAPL.EMAIL_FIELD).send_keys(EMAIL)
        self.find_element(PAPL.PASSWORD_FIELD).send_keys(PASSWORD)
        self.find_element(PAPL.ENTER_BUTTON).click()

    @allure.step('Получение текста последнего элемента из списка')
    def get_last_list_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        last_element = elements[-1]
        text_element = last_element.find_element(*OFL.LAST_ORDER_NUMBER)
        return text_element.text

    @allure.step('Получение текущего URL')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Ожидание изменения URL')
    def wait_until_url_changes(self, time=10):
        return WebDriverWait(self.driver, time).until(EC.url_changes(self.driver.current_url))

    @allure.step('Ожидание 2 секунды')
    def wait_two_sec(self):
        time.sleep(2)

    @allure.step('Имитация кнопки ESC')
    def escape_imitation(self):
        self.find_element(OFL.ORDER_NUMBER_MODAL)
        with allure.step(f'ESC button imitation'):
            try:
                ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
            except:
                pass

    @allure.step('Ожидание исчезновения элемента')
    def wait_element_disappear(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located((locator)))

    @allure.step('Ожидание необходимого текста в элементе')
    def text_in_element_presence(self, locator, text, time=10):
        WebDriverWait(self.driver, time).until(EC.text_to_be_present_in_element((locator), text))