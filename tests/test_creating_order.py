import json

import allure
import pytest

from conftest import prepare_data_order

from courier import API_Endpoints

class TestCreateOrder:
    @allure.title('Проверка заказа с разными цветами и без цвета')
    @pytest.mark.parametrize('color', [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_create_parametrize_order(self, prepare_data_order, color):
        prepare_data_order['color'] = color
        json_string = json.dumps(prepare_data_order)
        response = API_Endpoints().create_order(json_string)
        assert response.status_code == 201
        assert response.json().get('track') is not None





