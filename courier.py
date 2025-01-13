from datetime import timedelta

import allure

from constants import Constants
import requests
import random
import string
import datetime
from helpers import Helpers
from urls.urls import endpoint_courier, endpoint_login, endpoint_order


class API_Endpoints:
    host = Constants.HOST
    # метод создает данные для регистрации курьера
    def prepare_data(self):
        login = Helpers().generate_random_string(11)
        password = Helpers().generate_random_string(11)
        first_name = Helpers().generate_random_string(11)
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload

    @allure.step('Создаем курьера')
    def create_courier(self, data):
        url = f'{self.host}{endpoint_courier}'
        response = requests.post(url, data=data)
        return response

    @allure.step('ЛОгируем курьера')# метод логирует курьера
    def login_courier(self, data):
        url = f'{self.host}{endpoint_login}'
        response = requests.post(url, data = data)
        return response

    @allure.step('Удаляем созданного курьера')#  метод удаляет курьера
    def delete_courier(self,data):
        url = f'{self.host}{endpoint_courier}{data}'
        response = requests.delete(url)
        return response

    @allure.step('Создаем заказ')# метод создает заказ
    def create_order(self,data):
        url = f'{self.host}{endpoint_order}'
        response = requests.post(url, data=data)
        return response

    @allure.step('Создаем данные для заказа')#  метод создает данные для заказа (только обязательные поля)
    def prepare_data_order(self):
        firstName = Helpers().generate_random_string(10)
        lastName = Helpers().generate_random_string(10)
        address = Helpers().generate_random_string(10)
        metroStation = Helpers().generate_random_string(10)
        phone = Helpers().generate_random_phone_number(10)
        rentTime = random.randint(1,5)
        deliveryDate = (datetime.datetime.now() + timedelta(days=random.randint(1,21))).isoformat()
        comment = Helpers().generate_random_string(10)
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
    @allure.step('Вызываем список заказов')# метод GET для показывает список заказов
    def get_order_courier_list(self):
        url = f'{self.host}{endpoint_order}?limit=2&page=0&nearestStation=["1", "2"]'
        response = requests.get(url)
        return response

