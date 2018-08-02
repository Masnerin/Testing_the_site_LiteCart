# Задания по тестированию LiteCart.
# Сценарий проверки открытия новых окон
# в учебном приложении liteCart.

import pytest
from model.data_providers import admin


@pytest.mark.parametrize("admin", admin)
def test_opening_new_windows(app, admin):
    app.admin_login(admin)
    app.opening_new_windows()
