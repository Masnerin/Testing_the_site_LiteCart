from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart")
        return self

    @property
    def email_input(self):
        return self.driver.find_element_by_name("email")

    @property
    def password_input(self):
        return self.driver.find_element_by_name("password")

    @property
    def login_button(self):
        return self.driver.find_element_by_name("login")

    def logout(self):
        return self.driver.find_element_by_link_text("Logout").click()

    def product_selection(self):
        for j in range(1, 4):
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'li.product'))).click()
            size = self.driver.find_elements_by_css_selector('select')
            if len(size) != 0:
                Select(self.driver.find_element_by_css_selector('select')).select_by_index(1)
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[name="add_cart_product"]'))).click()
            self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'span.quantity'), str(j)))
        return

    def open_cart(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.link'))).click()
        return

    def product_removal(self):
        number_product = self.driver.find_elements_by_css_selector('li.shortcut')
        for i in range(0, len(number_product)):
            element = self.driver.find_elements_by_css_selector('table.dataTable.rounded-corners tr')
            a = len(element)
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[value=Remove]'))).click()
            self.wait.until(EC.staleness_of(element[a - 1]))
        return