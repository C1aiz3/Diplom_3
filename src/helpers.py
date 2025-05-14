from faker import Faker

fake = Faker('ru_RU')

class FakeData():

    @staticmethod
    def f_mail():
        return fake.email()