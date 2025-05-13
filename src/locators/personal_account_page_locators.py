from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:

    EMAIL_FIELD = By.XPATH, '//div[@class="input__container"]//input[@name="name"]' #поле Email
    PASSWORD_FIELD = By.XPATH, '//div[@class="input__container"]//input[@name="Пароль"]' #поле Password
    ENTER_BUTTON = By.XPATH, '//form/button' #кнопка Войти
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, '//nav/a' #кнопка Личный кабинет
    ORDER_HISTORY_BUTTON = By.XPATH, '//ul[@class="Account_list__3KQQf mb-20"]/li[2]/a' #кнопка История заказа в Личном кабинете
    EXIT_BUTTON = By.XPATH, '//li/button' #копка ВЫход в Личном кабинете