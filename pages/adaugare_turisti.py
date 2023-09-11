import time

from selenium.webdriver.common.by import By


class AdaugareTuristi:
    def __init__(self, driver):
        self.driver = driver
    def rezerva_rezervarea(self):
        scroll_distance = 1000
        self.driver.execute_script(f'window.scrollBy(0, {scroll_distance});')
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR,'[name="doar_salveaza"]').click()

