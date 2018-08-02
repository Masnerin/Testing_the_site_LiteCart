from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time


class CatalogPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
        return self

    def open_add_new_product(self):
        self.driver.get("http://localhost/litecart/admin/?category_id=0&app=catalog&doc=edit_product")
        return self

    def open_information(self):
        a = self.driver.find_elements_by_css_selector('ul.index a')
        a[1].click()
        return

    def open_prices(self):
        a = self.driver.find_elements_by_css_selector('ul.index a')
        a[3].click()
        return

    @property
    def status_enabled(self):
        return self.driver.find_element_by_name("status")

    @property
    def product_name_input(self):
        return self.driver.find_element_by_name("name[en]")

    @property
    def code_product_input(self):
        return self.driver.find_element_by_name("code")

    def product_group_selection(self):
        product_grups = self.driver.find_elements_by_name("product_groups[]")
        product_grups[2].click()
        return

    @property
    def quantity_input(self):
        quantity = self.driver.find_element_by_name("quantity")
        quantity.clear()
        return quantity

    def sold_out_status_selection(self):
        self.driver.find_element_by_css_selector('select[name=sold_out_status_id] option[value="2"]').click()
        return

    @property
    def image_input(self):
        return self.driver.find_element_by_name("new_images[]")

    @property
    def date_valid_from_input(self):
        return self.driver.find_element_by_name("date_valid_from")

    @property
    def date_valid_to_input(self):
        return self.driver.find_element_by_name("date_valid_to")

    def select_manufacturer_id(self):
        Select(self.driver.find_element_by_name("manufacturer_id")).select_by_index(1)
        return

    @property
    def keywords_input(self):
        return self.driver.find_element_by_name("keywords")

    @property
    def short_description_input(self):
        return self.driver.find_element_by_name("short_description[en]")

    @property
    def trumbowyg_editor_input(self):
        return self.driver.find_element_by_css_selector("div.trumbowyg-editor")

    @property
    def head_title_input(self):
        return self.driver.find_element_by_name("head_title[en]")

    @property
    def meta_description_input(self):
        return self.driver.find_element_by_name("meta_description[en]")

    @property
    def purchase_price_input(self):
        price = self.driver.find_element_by_name("purchase_price")
        price.clear()
        return price

    def currency_selection(self):
        self.driver.find_element_by_css_selector("select option[value=EUR]").click()
        return

    @property
    def price_usd_input(self):
        price_usd = self.driver.find_element_by_name("prices[USD]")
        price_usd.clear()
        return price_usd

    @property
    def price_eur_input(self):
        price_eur = self.driver.find_element_by_name("prices[EUR]")
        price_eur.clear()
        return price_eur

    def save_new_product(self):
        self.driver.find_element_by_name("save").click()
        return
