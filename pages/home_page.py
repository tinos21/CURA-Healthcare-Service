from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def click_make_appointment_button(self):
        make_appointment_button = self.driver.find_element(By.ID, 'btn-make-appointment')## locating the element
        make_appointment_button.click()

    def click_menu_and_go_home(self):
        pass  # Add locator and interaction logic here

    def click_menu_and_login(self):
        pass


