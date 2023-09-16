import time
import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

BUTTON_CAUTARE = 'cautare-btn1'

class CautaHotelPage:

    def __init__(self, driver):
        self.driver = driver

    def selecteaza_statiune(self,nume_statiune):
        self.driver.find_element(By.ID,'select2-fieldStatiune-container').click()
        self.driver.find_element(By.CSS_SELECTOR, '[type="search"]').send_keys(nume_statiune)
        self.driver.find_element(By.CSS_SELECTOR, '[type="search"]').send_keys(Keys.ENTER)

    def apasa_cautare(self):
        self.driver.find_element(By.ID,BUTTON_CAUTARE).click()

    def calendar_numar_luni_in_fata(self, numar_luni):
        self.driver.find_element(By.CSS_SELECTOR,'[id="checkIn"]').click()
        time.sleep(2)
        for _ in range(numar_luni):
            self.driver.find_element(By.CSS_SELECTOR,'[class="ui-icon ui-icon-circle-triangle-e"]').click()
        self.driver.find_element(By.CSS_SELECTOR,'#ui-datepicker-div > table > tbody > tr:nth-child(2) > td:nth-child(5) > a').click()
        self.apasa_cautare()

    def rezerva_camera_random(self):
        # Find all the elements that match your selector
        matches = self.driver.find_elements(By.CSS_SELECTOR,'a.btn.btn-primary.btn-sm.btn-book')

        # Check if there are any matches
        if matches:
            # Generate a random index within the range of the matches
            random_index = random.randint(0, len(matches) - 1)

            # Click on the element at the random index
            random_match = matches[random_index]
            random_match.click()

    def rezerva_camera_allotment_random(self):
        # Find elements that match the specified CSS selector
        elements = self.driver.find_elements(By.CSS_SELECTOR, 'td.disponibilitate-control > span')

        # Define the specific string you want to check for
        specific_string = 'disponibile'  # Replace with the string you're looking for

        # Create an empty list to store the positions (indices)
        positions = []

        # Iterate through the elements and check if they contain the specific string
        for index, element in enumerate(elements):
            title_attribute = element.get_attribute('title')
            if title_attribute and specific_string in title_attribute:
                positions.append(index + 1)  # Add one to the index and append to the list

        # Now you can use the positions obtained from the first selector in another selector or elsewhere in your code.
        # For example, you can use it to find elements in a different context:
        for position in positions:
            # Use the position in another selector or context
            other_selector = f'td.some-other-selector:nth-child({position})'
            # Do something with other_element
            self.driver.find_element(By.CSS_SELECTOR, f'tr:nth-child({position}) .btn-primary.btn-sm.btn-book').click()



