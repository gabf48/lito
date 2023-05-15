import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

BUTTON_ADAUGA_IN_COS = 'tr:nth-child(1) .fa-cart-arrow-down'
CAMP_CAUTA_CLIENT = 'mpf_inp_cauta'
LUPA_CAUTA_CLIENT = 'mpf_btn_cauta'
BUTTON_ADD_CLIENT = '[name="go_to_mwf_top"]'
BUTTON_SALVEAZA_PENTRU_OFERTARE = '[name="oferteaza"]'
NUMAR_CAMERE_DISPONIBILE = '.disponibilitate-control .x-available-room'

class HandleRezervare:

    def __init__(self, driver):
        self.driver = driver


    def apasa_adaugare_in_cos(self):
        self.driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        self.driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        self.driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, BUTTON_ADAUGA_IN_COS).click()

    def completeaza_adauga_client_existent_formular(self, nume_client_existent):
        self.driver.find_element(By.ID, CAMP_CAUTA_CLIENT).send_keys(nume_client_existent)
        time.sleep(2)
        self.driver.find_element(By.ID, LUPA_CAUTA_CLIENT).click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, BUTTON_ADD_CLIENT).click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, BUTTON_SALVEAZA_PENTRU_OFERTARE).click()

    def stocheaza_numere_camere_disponibile(self):
        NUMAR_CAMERE = self.driver.find_element(By.CSS_SELECTOR,NUMAR_CAMERE_DISPONIBILE).get_attribute('innerText')
        return NUMAR_CAMERE