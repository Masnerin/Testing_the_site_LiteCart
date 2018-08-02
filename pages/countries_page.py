from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import WebDriverWait


class CountriesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
        return self

    def number_of_countries(self):
        number_countries = self.driver.find_elements_by_css_selector('form[name=countries_form] tr.row')
        return number_countries

    def sorting_countries(self, number_countries):
        countries = []
        countries_sort = []
        for i in range(0, len(number_countries)):
            tds = number_countries[i].find_elements_by_css_selector('td')
            country = tds[4].get_attribute('textContent')
            countries.append(country)
            countries_sort.append(country)
        print("\n1. Количество стран на странице 'Countries':", len(countries))
        countries_sort.sort()
        for j in range(0, len(countries)):
            if countries[j] != countries_sort[j]:
                print("= Список стран не сортирован!")
                break
        print("= Список стран сортирован.")
        return countries

    def countries_with_zones(self, countries):
        number_countries = self.driver.find_elements_by_css_selector('form[name=countries_form] tr.row')
        for n in range(0, len(number_countries)):
            tds = number_countries[n].find_elements_by_css_selector('td')
            number_zones = tds[5].get_attribute('textContent')
            if int(number_zones) == 0:
                continue
            print("В стране", countries[n], "есть зоны.")
            number_countries[n].find_element_by_css_selector('a').click()
            trs_z = self.driver.find_elements_by_css_selector('table#table-zones tr')
            zones = []
            zones_sort = []
            for i in range(1, (len(trs_z) - 1)):
                tds_z = trs_z[i].find_elements_by_css_selector('td')
                zone = tds_z[2].get_attribute('textContent')
                zones.append(zone)
                zones_sort.append(zone)
            print("Количество найденных зон:", (len(zones) - 1))
            zones_sort.sort()
            for j in range(0, (len(zones) - 1)):
                if zones[j] != zones_sort[j]:
                    print("= Список зон не сортирован!")
                    break
            print("= Список зон сортирован.")
            self.driver.find_element_by_xpath("//*[text()='Countries']").click()
            number_countries = self.driver.find_elements_by_css_selector('form[name=countries_form] tr.row')

    def opening_the_country_creation_page(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.button'))).click()
        return

    def opening_new_windows(self):
        main_window = self.driver.current_window_handle
        old_windows = self.driver.window_handles
        links = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'i.fa.fa-external-link')))
        for i in range(0, len(links)):
            str_links = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'i.fa.fa-external-link')))
            str_links[i].click()
            self.wait.until(EC.new_window_is_opened(old_windows))
            new_windows = self.driver.window_handles
            result = list(set(new_windows) - set(old_windows))
            new_window = result[0]
            self.driver.switch_to.window(new_window)
            self.driver.close()
            self.driver.switch_to.window(main_window)
        return

