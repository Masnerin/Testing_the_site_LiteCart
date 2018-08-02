# Тестированию LiteCart.
# Проверка сортировки списков стран и зон.

import pytest
from model.data_providers import admin


@pytest.mark.parametrize("admin", admin)
def test_main_menu_admin(app, admin):
    app.admin_login(admin)
    app.sorting_countries()
    app.sorting_geo_zones()
