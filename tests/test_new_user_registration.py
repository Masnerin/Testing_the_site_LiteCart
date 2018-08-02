# Задания по тестированию LiteCart.
# Регистрация нового пользователя
# в учебном приложении liteCart.

import pytest
from model.data_providers import new_user


@pytest.mark.parametrize("customer", new_user)
def test_can_register_customer(app, customer):

    app.register_new_customer(customer)
    app.logout()
    app.login_new_user(customer)
    app.logout()
