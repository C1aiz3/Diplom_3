from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, '//li[1]/a' #кнопка Конструктор
    ORDERS_FEED_BUTTON = By.XPATH, '//li[2]/a' #кнопка Лента заказов
    FLUORESCENT_BUN = By.XPATH, '//ul[1]/a[1]' #Флюорисцентная булка
    INGREDIENT_COUNTER = By.XPATH, '//ul[1]/a[1]/div[1]/p' #счетчик ингредиентов
    DRAG_AND_DROP_FIELD = By.XPATH, '//li[1]/div' #поле для добавления ингредиента
    INGREDIENT_MODAL = By.XPATH, '//div[contains(@class, "pt-10 pb-15")]' #модальное окно ингредиента
    INGREDIENT_MODAL_CLOSE = By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]//button' #кнопка закрытия модального окна ингредиента
    ORDER_MODAL = By.XPATH, '//div/section/div[1]' #модальное окно заказа
    CLOSE_ORDER_MODAL = By.XPATH, '//button[contains(@class, "close_modified")]' #кнопка закрытия модального окна заказа
    MAKE_ORDER_BUTTON = By.XPATH, '//main/section//button' #кнопка Оформить заказ
    ING_MODAL_TITLE = By.XPATH, '//h2[contains(@class, "title_modified")]'