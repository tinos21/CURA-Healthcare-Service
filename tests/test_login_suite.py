import time

import pytest
from selenium.webdriver.common.by import By


from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.mark.usefixtures("setup_driver")
class TestLoginSuite:


    @pytest.mark.order(1)
    @pytest.mark.smoke
    def test_001_invalid_login(self):
        home_page = HomePage(self.driver, self.wait)  ### homepage initialization
        home_page.click_make_appointment_button()
        login_page = LoginPage(self.driver, self.wait)  ## loginpage initialization

        h2_tag = self.driver.find_element(By.TAG_NAME, 'h2')  # checking to make login indeed showed up
        assert h2_tag.text == "Login", f"Expected 'Login', but got {h2_tag.text}"
        time.sleep(3)
        ##### starting to enter login information
        login_page.click_username_field("John Doe")
        login_page.click_password_field("ThisIsNot")
        time.sleep(2)
        time.sleep(2)
        login_page.click_login_button()
        time.sleep(6)
        h2_tag_2 = self.driver.find_element(By.CSS_SELECTOR, '.lead.text-danger')  ## locating the second element
        assert h2_tag_2.text == "Login failed! Please ensure the username and password are valid.", f"expected 'Login failed! Please ensure the username and password are valid.' but got {h2_tag_2.text}"
        time.sleep(5)


    @pytest.mark.order(2)
    @pytest.mark.regression
    def test_002_valid_login(self):
        home_page = HomePage(self.driver , self.wait)    ### homepage initialization
        home_page.click_make_appointment_button()
        login_page = LoginPage(self.driver, self.wait ) ## loginpage initialization

        h2_tag = self.driver.find_element(By.TAG_NAME, 'h2')  # checking to make login indeed showed up
        assert h2_tag.text == "Login", f"Expected 'Login', but got {h2_tag.text}"
        time.sleep(3)
        ##### starting to enter login information
        login_page.click_username_field("John Doe")
        login_page.click_password_field("ThisIsNotAPassword")
        time.sleep(2)
        login_page.click_login_button()
        time.sleep(6)
        h2_tag_2 = self.driver.find_element(By.TAG_NAME, 'h2') ## locating the second element

        assert h2_tag_2.text == "Make Appointment", f"expected 'Make Appointment' but got {h2_tag_2.text}"
        time.sleep(5)














