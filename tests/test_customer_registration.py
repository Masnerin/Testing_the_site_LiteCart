# Тестирование LiteCart.
# Добавление нового пользователя.

import pytest
from model.data_providers import new_customer


@pytest.mark.parametrize("customer", new_customer, ids=[repr(x) for x in new_customer])
def test_can_register_customer(app, customer):

    old_ids = app.get_customer_ids(customer)
    app.register_new_customer(customer)
    new_ids = app.get_customer_ids(customer)

    assert all([i in new_ids for i in old_ids])
    assert len(new_ids) == len(old_ids) + 1
