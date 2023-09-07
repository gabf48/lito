from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self,url,username,password):
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.find_element(By.CSS_SELECTOR,'[name="username"]').send_keys(username)
        self.driver.find_element(By.ID,'inputPassword').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR,'[name="auth_login"]').click()