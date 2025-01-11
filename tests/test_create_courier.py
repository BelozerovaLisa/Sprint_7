import allure
import pytest

from conftest import prepare_user, user_data
from constants import Constants
from courier import API_Endpoints

class TestCreateCourier:
    @allure.title('Проверка что курьера можно создать')
    def test_create(self, prepare_user):
        get_data_courier = prepare_user
        assert get_data_courier.json() == Constants.response_test_create_courier
        assert get_data_courier.status_code == 201


    @allure.title('Проверка на создание 2х одинаковых курьеров с одинаковыми данными')
    def test_required_fields(self, user_data):
        API_Endpoints().create_courier(user_data)
        get_data_courier = API_Endpoints().create_courier(user_data)
        assert get_data_courier.status_code == 409
        assert get_data_courier.json()['message'] == Constants.response_test_login_already_exist
        id = API_Endpoints().login_courier(user_data)
        API_Endpoints().delete_courier(id)


    @allure.title('Проверка на создание курьера, со передачей в запрос не всех обязательных параметров')#
    @pytest.mark.parametrize('field', ['login','password'])
    def test_required_field(self,user_data, field):
        del user_data[field]
        get_data_courier = API_Endpoints().create_courier(user_data)
        assert get_data_courier.status_code == 400
        assert get_data_courier.json()['message'] == Constants.response_test_not_create_courier

    @allure.title('Проверка на создание пользователя с логином, который уже есть')
    def test_create_courier_with_equal_login(self, user_data):
        API_Endpoints().create_courier(user_data)
        data = API_Endpoints().prepare_data()
        data['login'] = user_data['login']
        get_data_courier = API_Endpoints().create_courier(data)
        assert get_data_courier.status_code == 409
        assert get_data_courier.json()['message'] == Constants.response_test_login_already_exist
        id = API_Endpoints().login_courier(user_data)
        API_Endpoints().delete_courier(id)
