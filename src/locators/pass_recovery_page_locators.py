from selenium.webdriver.common.by import By

class PassRecoveryPageLocators:

    AUTH_FORGOT_PASS_BUTTON = By.XPATH, '//div/p[2]/a[@class="Auth_link__1fOlj"]'                #Кнопка "Восстановить пароль" на странице авторизации
    RECOVERY_FORGOT_PASS_BUTTON = By.XPATH, '//form//button'                                     #Кнопка "Восстановить" на странице восстановления
    EMAIL_FIELD_Recovery_PAGE = By.XPATH, '//div[@class="input__container"]//input'              #Поле "EMAIL" на странице восстановления
    SHOW_HIDE_PASS_BUTTON = By.XPATH, '//div[@class="input__icon input__icon-action"]'           #Кнопка показать\скрыть пароль
    PASS_FIELD = By.XPATH, '//input[@name="Введите новый пароль"]'                               #Поле "Пароль"



