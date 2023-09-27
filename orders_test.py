import stand_request

#Анатолий Шулежко, 8а кагорта - Финальный проект. Инженер по тестированию плюс.

# Проверяем, что код ответа равен 200
def test_positive_assert():
    order_response = stand_request.get_an_orders(stand_request.track_number)
    assert order_response.status_code == 200






