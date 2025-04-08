

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




class AppointmentConfirmationPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    #### confirmation message locator
    def confirmation_message(self):
        return (By.XPATH, "//h1[contains(text(), 'Appointment Confirmation')]")

    # 'Back to Home' locator
    def back_to_home_button(self):
        return (By.XPATH, "//button[contains(text(), 'Back to Home')]")

    # Method to get confirmation message
    def get_confirmation_message(self):
        confirmation_message = self.wait.until(
            EC.presence_of_element_located(self.confirmation_message())
        )
        return confirmation_message.text

    # Method to click the 'Back to Home' button
    def click_back_to_home(self):
        back_to_home_button = self.wait.until(
            EC.element_to_be_clickable(self.back_to_home_button())
        )
        back_to_home_button.click()



