
import pytest

from courier import API_Endpoints

# фикстура создает пользовательские данные
@pytest.fixture()
def user_data():
    return API_Endpoints().prepare_data()
# фикстура создает пользовательские данные без имени пользователя
@pytest.fixture()
def prepare_login_password(user_data):
    API_Endpoints().create_courier(user_data)
    del user_data['firstName']
    return user_data
# фикстура создает и удаляет пользователя после выполнения регистрации
@pytest.fixture()
def prepare_user(user_data):
    print(user_data)
    courier = API_Endpoints().create_courier(user_data)
    login = API_Endpoints().login_courier(user_data)
    yield courier
    API_Endpoints().delete_courier(login.json()['id'])
# фикстура создает и удаляет пользователя после логирования
@pytest.fixture()
def prepare_user_login(user_data):
    print(user_data)
    courier = API_Endpoints().create_courier(user_data)
    login = API_Endpoints().login_courier(user_data)
    yield login
    API_Endpoints().delete_courier(login)
# фикстура создает данные для заказа самоката
@pytest.fixture()
def prepare_data_order():
    return API_Endpoints().prepare_data_order()

