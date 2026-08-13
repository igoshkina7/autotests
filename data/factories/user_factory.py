from faker import Faker

fake = Faker()

class UserFactory:

    @staticmethod
    def create():
        return {
            "name": fake.name(),
            "email": fake.email(),
            "password": "abracadabra12345678"
        }