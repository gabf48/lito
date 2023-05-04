import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

BUTTON_ADAUGA_IN_COS = 'tr:nth-child(1) .fa-cart-arrow-down'

class HandleRezervare:

    def __init__(self, driver):
        self.driver = driver

    def apasa_adaugare_in_cos(self):
        self.driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        self.driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        self.driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.DOWN)
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, BUTTON_ADAUGA_IN_COS).click()