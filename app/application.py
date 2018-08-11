from selenium import webdriver
from pages.home_page import HomePage
from pages.admin_panel_login_page import AdminPanelLoginPage
from pages.admin_page import AdminPage
from pages.customer_list_page import CustomerListPage
from pages.create_account_page import CreateAccountPage
from pages.countries_page import CountriesPage
from pages.geo_zones_page import GeoZonesPage
from pages.catalog_page import CatalogPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)
        self.create_account_page = CreateAccountPage(self.driver)
        self.admin_panel_login_page = AdminPanelLoginPage(self.driver)
        self.admin_page = AdminPage(self.driver)
        self.customer_list_page = CustomerListPage(self.driver)
        self.countries_page = CountriesPage(self.driver)
        self.geo_zones_page = GeoZonesPage(self.driver)
        self.catalog_page = CatalogPage(self.driver)

    def quit(self):
        self.driver.quit()

    def admin_login(self, admin):
        if self.admin_panel_login_page.open().is_on_this_page():
            self.admin_panel_login_page.username_input.send_keys(admin.username)
            self.admin_panel_login_page.password_input.send_keys(admin.password)
            self.admin_panel_login_page.submit_login()
        return

    def logout(self):
        self.home_page.logout()

    def login_new_user(self, customer):
        self.home_page.email_input.send_keys(customer.email)
        self.home_page.password_input.send_keys(customer.password)
        self.home_page.login_button.click()

    def all_main_menu_items(self):
        items = self.admin_page.number_of_menu_items()
        for i in range(0, items):
            menu_items = self.admin_page.menu_items()
            menu_items[i].click()
            sub_items = self.admin_page.number_of_menu_sub_items()
            if sub_items == 0:
                continue
            for j in range(0, sub_items):
                menu_sub_items = self.admin_page.menu_sub_items()
                menu_sub_items[j].click()

    def sorting_countries(self):
        self.countries_page.open()
        number_countries = self.countries_page.number_of_countries()
        countries = self.countries_page.sorting_countries(number_countries)
        self.countries_page.countries_with_zones(countries)

    def sorting_geo_zones(self):
        self.geo_zones_page.open()
        number_geo_zones = self.geo_zones_page.number_of_geo_zones()
        geo_zones = self.geo_zones_page.sorting_geo_zones(number_geo_zones)
        self.geo_zones_page.geo_zones_with_zones(geo_zones)

    def register_new_customer(self, customer):
        self.create_account_page.open()
        self.create_account_page.firstname_input.send_keys(customer.firstname)
        self.create_account_page.lastname_input.send_keys(customer.lastname)
        self.create_account_page.address1_input.send_keys(customer.address)
        self.create_account_page.postcode_input.send_keys(customer.postcode)
        self.create_account_page.city_input.send_keys(customer.city)
        self.create_account_page.select_country(customer.country)
        self.create_account_page.select_zone(customer.zone)
        self.create_account_page.email_input.send_keys(customer.email)
        self.create_account_page.phone_input.send_keys(customer.phone)
        self.create_account_page.password_input.send_keys(customer.password)
        self.create_account_page.confirmed_password_input.send_keys(customer.password)
        self.create_account_page.create_account_button.click()

    def add_new_product(self, new_product):
        self.catalog_page.open_add_new_product()
        self.catalog_page.status_enabled.click()
        self.catalog_page.product_name_input.send_keys(new_product.product_name)
        self.catalog_page.code_product_input.send_keys(new_product.code_product)
        self.catalog_page.product_group_selection()
        self.catalog_page.quantity_input.send_keys(new_product.quantity)
        self.catalog_page.sold_out_status_selection()
        self.catalog_page.image_input.send_keys(new_product.image)
        self.catalog_page.date_valid_from_input.send_keys(new_product.date_valid_from)
        self.catalog_page.date_valid_to_input.send_keys(new_product.date_valid_to)
        self.catalog_page.open_information()
        self.catalog_page.select_manufacturer_id()
        self.catalog_page.keywords_input.send_keys(new_product.keywords)
        self.catalog_page.short_description_input.send_keys(new_product.short_description)
        self.catalog_page.trumbowyg_editor_input.send_keys(new_product.trumbowyg_editor)
        self.catalog_page.head_title_input.send_keys(new_product.head_title)
        self.catalog_page.meta_description_input.send_keys(new_product.meta_description)
        self.catalog_page.open_prices()
        self.catalog_page.purchase_price_input.send_keys(new_product.purchase_price)
        self.catalog_page.currency_selection()
        self.catalog_page.price_usd_input.send_keys(new_product.prices_usd)
        self.catalog_page.price_eur_input.send_keys(new_product.prices_eur)
        self.catalog_page.save_new_product()

    def get_customer_ids(self, customer):
        if self.admin_panel_login_page.open().is_on_this_page():
            self.admin_panel_login_page.username_input.send_keys(customer.username1)
            self.admin_panel_login_page.password_input.send_keys(customer.password1)
            self.admin_panel_login_page.submit_login()
        return self.customer_list_page.open().get_customer_ids()

    def product_in_the_cart(self):
        self.home_page.open()
        self.home_page.product_selection()

    def clear_to_cart(self):
        self.home_page.open_cart()
        self.home_page.product_removal()

    def opening_new_windows(self):
        self.countries_page.open()
        self.countries_page.opening_the_country_creation_page()
        self.countries_page.opening_new_windows()
