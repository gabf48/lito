from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class CautaHotelPage:

    def __init__(self, driver):
        self.driver = driver

    def selecteaza_statiune(self,nume_statiune):
        open_dropdown = self.driver.find_element(By.ID,'select2-fieldStatiune-container').click()
        type_statiune_name = self.driver.find_element(By.CSS_SELECTOR, '[type="search"]').send_keys(nume_statiune)
        type_statiune_name = self.driver.find_element(By.CSS_SELECTOR, '[type="search"]').send_keys(Keys.ENTER)
