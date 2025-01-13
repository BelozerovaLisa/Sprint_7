
import allure

from courier import API_Endpoints


class TestGETOrderList:
    @allure.title('Проверка получения списка заказов')
    def test_get_order_list(self):
        response = API_Endpoints().get_order_courier_list()
        assert response.status_code == 200
        assert len(response.json().get("orders")) > 0
