from datetime import timedelta
from constants import Constants
import requests
import random
import string
import datetime

class API_Endpoints:
    host = Constants.HOST
    # метод создает данные для регистрации курьера
    def prepare_data(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload

    # метод создает курьера
    def create_courier(self, data):
        url = f'{self.host}/api/v1/courier'
        response = requests.post(url, data=data)
        return response
    # метод логирует курьера
    def login_courier(self, data):
        url = f'{self.host}/api/v1/courier/login'
        response = requests.post(url, data = data)
        return response
    #  метод удаляет курьера
    def delete_courier(self,data):
        url = f'{self.host}/api/v1/courier/{data}'
        response = requests.delete(url)
        return response
    # метод создает заказ
    def create_order(self,data):
        url = f'{self.host}/api/v1/orders'
        response = requests.post(url, data=data)
        return response

    #  метод создает данные для заказа (только обязательные поля)
    def prepare_data_order(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        def generate_random_phone_number(length):
            random_string = ''.join(str(random.randint(0,9)) for i in range(length))
            return int(random_string)
        firstName = generate_random_string(10)
        lastName = generate_random_string(10)
        address = generate_random_string(10)
        metroStation = generate_random_string(10)
        phone = generate_random_phone_number(10)
        rentTime = random.randint(1,5)
        deliveryDate = (datetime.datetime.now() + timedelta(days=random.randint(1,21))).isoformat()
        comment = generate_random_string(10)
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "address": address,
            "metroStation": metroStation,
            "phone": phone,
            "rentTime": rentTime,
            "deliveryDate": deliveryDate,
            "comment": comment
        }
        return payload
    # метод GET для показывает список заказов
    def get_order_courier_list(self):
        url = f'{self.host}/api/v1/orders?limit=1&page=0'
        response = requests.get(url)
        return response

