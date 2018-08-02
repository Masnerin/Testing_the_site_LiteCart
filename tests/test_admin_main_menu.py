# Тестирование LiteCart.
# Тестирование элементов главного меню админки.

import pytest
from model.data_providers import admin


@pytest.mark.parametrize("admin", admin)
def test_main_menu_admin(app, admin):
    app.admin_login(admin)
    app.all_main_menu_items()
