from selenium.webdriver.common.by import By


class Asserts:

    def __init__(self, driver):
        self.driver = driver

    def verifica_exitenta_selector_pe_pagina(self, selector):
        element = self.driver.find_element(By.CSS_SELECTOR, selector)
        assert element.is_displayed()