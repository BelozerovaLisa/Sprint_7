import allure
import pytest

from conftest import prepare_user, user_data
from constants import Constants
from courier import API_Endpoints

class TestCreateCourier:
    api = API_Endpoints()
    @allure.title('Проверка что курьера можно создать')
    def test_create(self, user_data):
        get_data_courier = self.api.create_courier(user_data)
        assert get_data_courier.json() == Constants.response_test_create_courier
        assert get_data_courier.status_code == 201
        id = self.api.login_courier(user_data)
        self.api.delete_courier(id.json()["id"])


    @allure.title('Проверка на создание 2х одинаковых курьеров с одинаковыми данными')
    def test_required_fields(self, user_data):
        self.api.create_courier(user_data)
        get_data_courier = self.api.create_courier(user_data)
        assert get_data_courier.status_code == 409
        assert get_data_courier.json()['message'] == Constants.response_test_login_already_exist
        id = self.api.login_courier(user_data)
        self.api.delete_courier(id.json()["id"])


    @allure.title('Проверка на создание курьера, с передачей в запрос не всех обязательных параметров')#
    @pytest.mark.parametrize('field', ['login','password'])
    def test_required_field(self,user_data, field):
        del user_data[field]
        get_data_courier = self.api.create_courier(user_data)
        assert get_data_courier.status_code == 400
        assert get_data_courier.json()['message'] == Constants.response_test_not_create_courier

    @allure.title('Проверка на создание пользователя с логином, который уже есть')
    def test_create_courier_with_equal_login(self, user_data):
        self.api.create_courier(user_data)
        data = self.api.prepare_data()
        data['login'] = user_data['login']
        get_data_courier = self.api.create_courier(data)
        assert get_data_courier.status_code == 409
        assert get_data_courier.json()['message'] == Constants.response_test_login_already_exist
        id = self.api.login_courier(user_data)
        self.api.delete_courier(id.json()["id"])
