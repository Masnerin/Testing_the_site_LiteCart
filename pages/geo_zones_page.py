from selenium.webdriver.support.wait import WebDriverWait


class GeoZonesPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
        return self

    def number_of_geo_zones(self):
        trs = self.driver.find_elements_by_css_selector('form[name=geo_zones_form] tr.row')
        return trs

    def sorting_geo_zones(self, trs):
        geo_zones = []
        geo_zones_sort = []
        for i in range(0, len(trs)):
            tds = trs[i].find_elements_by_css_selector('td')
            geo_zone = tds[2].get_attribute('textContent')
            geo_zones.append(geo_zone)
            geo_zones_sort.append(geo_zone)
        print("\n2. Количество гео-зон на странице 'Geo Zones':", len(geo_zones))
        geo_zones_sort.sort()
        for j in range(0, len(geo_zones)):
            if geo_zones[j] != geo_zones_sort[j]:
                print("= Список гео-зон не сортирован!")
                break
        print("= Список гео-зон сортирован.")
        return geo_zones

    def geo_zones_with_zones(self, geo_zones):
        number_geo_zones = self.driver.find_elements_by_css_selector('form[name=geo_zones_form] tr.row')
        for n in range(0, len(number_geo_zones)):
            tds = number_geo_zones[n].find_elements_by_css_selector('td')
            number_zones = tds[3].get_attribute('textContent')
            if int(number_zones) == 0:
                continue
            print("В гео-зоне", geo_zones[n], "есть зоны.")
            number_geo_zones[n].find_element_by_css_selector('a').click()
            trs_z = self.driver.find_elements_by_css_selector('table#table-zones tr')
            zones = []
            zones_sort = []
            for i in range(1, (len(trs_z) - 1)):
                tds_z = trs_z[i].find_elements_by_css_selector('td')
                zone = tds_z[2].find_element_by_css_selector('option[selected=selected]').get_attribute('textContent')
                zones.append(zone)
                zones_sort.append(zone)
            print("Количество найденных зон:", len(zones))
            zones_sort.sort()
            for j in range(1, (len(zones) - 1)):
                if zones[j] != zones_sort[j]:
                    print("= Список зон не сортирован!")
                    break
            print("= Список зон сортирован.")
            self.driver.find_element_by_xpath("//*[text()='Geo Zones']").click()
            number_geo_zones = self.driver.find_elements_by_css_selector('form[name=geo_zones_form] tr.row')
