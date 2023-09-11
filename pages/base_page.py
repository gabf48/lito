from selenium.webdriver.common.by import By
import pyautogui


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def assert_if_element_is_display_on_the_page(self, selector):
        elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
        return len(elements) > 0 and elements[0].is_displayed()

    def is_text_displayed(self, text_to_check):
        page_text = self.driver.page_source
        return text_to_check in page_text
    def zoom_out(self, zoom_out_count):
        for _ in range(zoom_out_count):
            pyautogui.keyDown('ctrl')  # Press the Ctrl key (Windows/Linux)
            pyautogui.press('-')  # Press the '-' key
            pyautogui.keyUp('ctrl')

    def zoom_in(self, zoom_out_count):
        for _ in range(zoom_out_count):
            pyautogui.keyDown('ctrl')  # Press the Ctrl key (Windows/Linux)
            pyautogui.press('+')  # Press the '-' key
            pyautogui.keyUp('ctrl')