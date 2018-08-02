# Тестирование LiteCart.
# Проверка добавления нового товара
# в учебном приложении liteCart.

import pytest
from model.data_providers import admin, new_product


@pytest.mark.parametrize("new_product", new_product)
def test_create_new_product(app, new_product):
    app.admin_login(new_product)
    app.add_new_product(new_product)
