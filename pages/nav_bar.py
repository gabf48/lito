import time

from selenium.webdriver.common.by import By


class NavBar:

    def __init__(self, driver):
        self.driver = driver

    def select_specific_page_from_nav_bar(self, item_name):

        list_elements = self.driver.find_elements(By.CSS_SELECTOR, ".navbar-nav.mr-auto li > a")

        for element in list_elements:
            element_text = element.text
            print("Element Text:", element_text)

            if item_name in element_text:
                element.click()
                break
