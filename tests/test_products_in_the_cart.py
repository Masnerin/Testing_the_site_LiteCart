# Тестирование LiteCart.
# Сценарий для добавления товаров в корзину
# и удаления товаров из корзины.
# в учебном приложении liteCart.


def test_product_in_the_cart(app):
    app.product_in_the_cart()
    app.clear_to_cart()
