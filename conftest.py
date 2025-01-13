
import pytest

from courier import API_Endpoints

api = API_Endpoints()
# фикстура создает пользовательские данные
@pytest.fixture()
def user_data():
    return api.prepare_data()
# фикстура создает пользовательские данные без имени пользователя
@pytest.fixture()
def prepare_login_password(user_data):
    api.create_courier(user_data)
    del user_data['firstName']
    return user_data
# фикстура создает и удаляет пользователя после выполнения регистрации
@pytest.fixture()
def prepare_user(user_data):
    courier = api.create_courier(user_data)
    login = api.login_courier(user_data)
    yield (courier, login)
    api.delete_courier(login.json()['id'])
# фикстура создает и удаляет пользователя после логирования
# фикстура создает данные для заказа самоката
@pytest.fixture()
def prepare_data_order():
    return api.prepare_data_order()

