import time

from selenium.webdriver.common.by import By


class AdaugaClient:

    def __init__(self, driver):
        self.driver = driver

    def adauga_client(self, email):
        self.driver.find_element(By.CSS_SELECTOR, '[id="mpf_inp_cauta"]').send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, '#main_persoana_fizica .fa-search').click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, '[class="btn btn-sm btn-outline-primary mwf_btn_select"]').click()
        self.driver.find_element(By.CSS_SELECTOR, '[value="Rezerva"]').click()
