from faker import Faker


URL = 'https://stellarburgers.nomoreparties.site/'
EMAIL = 'pavel_tishenko_19_999@mail.ru'
PASSWORD = '1234567890'

fake = Faker('ru_RU')


class FakeData():

    @staticmethod
    def f_mail():
        return fake.email()