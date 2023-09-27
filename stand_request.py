import requests
import configuration
import data


# Запрос на создание нового заказа
def post_new_order(orders_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                    json=orders_body,
                    headers=data.headers)
response = post_new_order(data.orders_body)
track_number = response.json()["track"]  # Сохранение трeк номера в переменную

# Запрос на получение заказа по трек номеру
def get_an_orders(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_AN_ORDERS,
                        params={"t": track_number})