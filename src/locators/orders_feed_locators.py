from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    SOME_ORDER = By.XPATH, '//main//li[1]/a' #Верхний заказ на главной
    ORDER_MODAL = By.XPATH, '//section[2]/div/div' #модальное окно заказа
    ORDER_MODAL_CLOSE = By.XPATH, '//section[contains(@class, "modal_opened")]//button' #кнопка закрытия модального окна заказа
    ORDER_NUMBER_MODAL = By.XPATH, '//div/section/div//h2' #номер заказа на модальном окне
    LAST_ORDER_NUMBER = By.XPATH, '//div[contains(@class, "orderHistory")]//li[position()=last()]//div[contains(@class, "textBox")]/p[1]' #последний заказ в Истории заказов Личного кабинета
    ACTUAL_ORDER_NUMBER = By.XPATH, '//a[contains(@class, "link__1iNby")]/div/p[1]' #актуальный номер заказа в Ленте заказов
    TOTAL_ORDERS_COUNTER = By.XPATH, '//div[contains(@class, "undefined")]/p[2]' #заказов за все время
    TODAY_ORDERS_COUNTER = By.XPATH, '//div[contains(@class, "OrderFeed")]/div[3]/p[2]' #заказов сегодня
    IN_PROGRESS_SECTION = By.XPATH, '//ul[2]/li[contains(@class, "digits-default")]' #заказы в работе

