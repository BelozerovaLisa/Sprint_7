import allure
import pytest

from conftest import user_data, prepare_user_login, prepare_login_password
from constants import Constants

from courier import API_Endpoints


class TestLoginCourier:
    @allure.title('Проверка курьер может войти по логину и паролю')
    def test_login(self, prepare_user_login):
        get_data_courier = prepare_user_login
        assert get_data_courier.json().get('id') is not None
        assert get_data_courier.status_code == 200

    @allure.title('Проверка на запрос логирования курьера без логина или пароля')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_required_field_login(self, prepare_login_password, field):
        del prepare_login_password[field]
        get_data_courier = API_Endpoints().login_courier(prepare_login_password)
        assert get_data_courier.status_code == 400
        assert get_data_courier.json()['message'] == Constants.response_test_login_not_enough

    @allure.title('Проверка на запрос логирования с несуществующей парой логин-пароль')
    def test_login_not_exist(self,user_data):
        del user_data['firstName']
        response = API_Endpoints().login_courier(user_data)
        assert response.status_code == 404
        assert response.json()['message'] == Constants.response_test_login_not_found

    @allure.title('Проверка вернет ли система ошибку если неправильно указать логин или пароль')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_required_field_login(self, prepare_login_password, field):
        prepare_login_password[field] = 'test'
        get_data_courier = API_Endpoints().login_courier(prepare_login_password)
        assert get_data_courier.status_code == 404
        assert get_data_courier.json()['message'] == Constants.response_test_login_not_found

