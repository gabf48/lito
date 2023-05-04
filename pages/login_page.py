from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self,url,username,password):
        self.driver.maximize_window()
        self.driver.get(url)
        username_input = self.driver.find_element(By.CSS_SELECTOR,'[name="username"]').send_keys(username)
        password_input = self.driver.find_element(By.ID,'inputPassword').send_keys(password)
        login_button = self.driver.find_element(By.CSS_SELECTOR,'[name="auth_login"]').click()