from selenium.webdriver.support.wait import WebDriverWait


class AdminPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/admin")
        return self

    def menu_items(self):
        return self.driver.find_elements_by_css_selector('li#app-')

    def number_of_menu_items(self):
        a = self.driver.find_elements_by_css_selector('li#app-')
        items = len(a)
        return items

    def menu_sub_items(self):
        return self.driver.find_elements_by_css_selector('ul.docs a')

    def number_of_menu_sub_items(self):
        b = self.driver.find_elements_by_css_selector('ul.docs a')
        sub_items = len(b)
        return sub_items

