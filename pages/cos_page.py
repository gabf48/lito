from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

NUMAR_CAMERE_COS = '[href="#cart_rez"]'
class Cos:

    def __init__(self, driver):
        self.driver = driver


    def deschide_cos(self):
        self.driver.find_element(By.CSS_SELECTOR,NUMAR_CAMERE_COS).click()

    def verifica_numar_camere_cos(self, expected_numere_camere):
        nr_camere = self.driver.find_element(By.CSS_SELECTOR, NUMAR_CAMERE_COS).get_attribute('innerText')
        print(nr_camere)
        assert expected_numere_camere in nr_camere

    def sterge_camera(self):
        self.driver.find_element(By.CSS_SELECTOR,'#js-inscrieri > tr:nth-child(1) > td:nth-child(11) > a').click()
        alert = Alert(self.driver)
        alert.accept()

