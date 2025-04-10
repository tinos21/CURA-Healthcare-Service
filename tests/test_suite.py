import time

import pytest
from selenium.webdriver.common.by import By

from pages.appointment_page import AppointmentPage
from pages.home_page import HomePage
from pages.login_page import LoginPage



@pytest.mark.dependency()
@pytest.mark.usefixtures("setup_driver")
class TestLoginSuite:

    @pytest.mark.order(1)
    @pytest.mark.smoke
    def test_001_invalid_login_empty_fields(self):
        home_page = HomePage(self.driver, self.wait)  ### homepage initialization
        home_page.click_make_appointment_button()
        login_page = LoginPage(self.driver, self.wait)  ## loginpage initialization

        h2_tag = self.driver.find_element(By.TAG_NAME, 'h2')  # checking to make login indeed showed up as a title
        assert h2_tag.text == "Login", f"Expected 'Login', but got {h2_tag.text}"
        time.sleep(3)
        ##### starting to enter login information
        login_page.click_username_field("")
        login_page.click_password_field("")
        time.sleep(2)
        time.sleep(2)
        login_page.click_login_button()
        time.sleep(6)
        h2_tag_2 = self.driver.find_element(By.CSS_SELECTOR, '.lead.text-danger')  ## locating the second element
        assert h2_tag_2.text == "Make Appointment", f"expected 'Make Appointment' but got {h2_tag_2.text}"
        time.sleep(5)

    @pytest.mark.order(2)
    def test_002_invalid_login_username(self):
        home_page = HomePage(self.driver, self.wait)  ### homepage initialization
        home_page.click_make_appointment_button()
        login_page = LoginPage(self.driver, self.wait)  ## loginpage initialization

        h2_tag = self.driver.find_element(By.TAG_NAME, 'h2')  # checking to make login indeed showed up
        assert h2_tag.text == "Login", f"Expected 'Login', but got {h2_tag.text}"
        time.sleep(3)
        ##### starting to enter login information
        login_page.click_username_field("Jojo")
        login_page.click_password_field("ThisIsNotAPassword")
        time.sleep(2)
        time.sleep(2)
        login_page.click_login_button()
        time.sleep(6)
        h2_tag_3 = self.driver.find_element(By.CSS_SELECTOR, '.lead.text-danger')  ## locating the second element
        assert h2_tag_3.text == "Make Appointment", f"expected 'Make Appointment' but got {h2_tag_3.text}"
        time.sleep(5)

    @pytest.mark.order(3)
    def test_003_invalid_login_password(self):
        home_page = HomePage(self.driver, self.wait)  ### homepage initialization
        home_page.click_make_appointment_button()
        login_page = LoginPage(self.driver, self.wait)  ## loginpage initialization

        h2_tag = self.driver.find_element(By.TAG_NAME, 'h2')  # checking to make login indeed showed up
        #assert h2_tag.text == "Login", f"Expected 'Login', but got {h2_tag.text}"
        time.sleep(3)
        ##### starting to enter login information
        login_page.click_username_field("John Doe")
        login_page.click_password_field("ThisIsNotnnnnn")
        time.sleep(2)
        time.sleep(2)
        login_page.click_login_button()
        time.sleep(6)
        h2_tag_4 = self.driver.find_element(By.CSS_SELECTOR, '.lead.text-danger')  ## locating the second element
        assert h2_tag_4.text == "Make Appointment.", f"expected 'Make Appointment' but got {h2_tag_4.text}"
        time.sleep(5)


    @pytest.mark.order(4)
    @pytest.mark.regression
    @pytest.mark.dependency(name="valid_login")
    def test_004_valid_login(self):
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
        h2_tag_5 = self.driver.find_element(By.TAG_NAME, 'h2') ## locating the second element

        assert h2_tag_5.text == "Make Appointment", f"expected 'Make Appointment' but got {h2_tag_5.text}"
        time.sleep(1)

    @pytest.mark.smoke
    @pytest.mark.order(5)
    @pytest.mark.dependency(depends=["valid_login"])
    def test_005_invalid_appointment_scheduling_no_calender_selected(self):
        appointment = AppointmentPage(self.driver, self.wait)
        self.driver.refresh()
        appointment.click_facility_dropdown()
        time.sleep(4)
        appointment.select_apply_for_hospital_readmission_checkmark()
        appointment.click_medicare_radio_button()
        ##appointment.calendar("08/04/2025")
        appointment.write_in_comment_box("hello my name is tino i would like to schedule an appointment")
        time.sleep(4)
        appointment.click_book_appointment()
        time.sleep(5)
        h2_tag_6 = self.driver.find_element(By.TAG_NAME, 'h2') ## select a locator for text on top of page
        assert h2_tag_6.text == "Appointment Confirmation", f"expected 'Appointment Confirmation' but got {h2_tag_6.text}"

    @pytest.mark.smoke
    @pytest.mark.order(6)
    @pytest.mark.dependency(depends=["valid_login"])
    def test_006_invalid_appointment_scheduling_zero_value_inserted(self):
        appointment = AppointmentPage(self.driver, self.wait)
        self.driver.refresh()
        appointment.click_facility_dropdown()
        time.sleep(4)
        appointment.select_apply_for_hospital_readmission_checkmark()
        appointment.click_medicare_radio_button()
        appointment.calendar("00/00/0000")
        appointment.write_in_comment_box("hello my name is tino i would like to schedule an appointment")
        time.sleep(4)
        appointment.click_book_appointment()
        time.sleep(5)
        h2_tag_7 = self.driver.find_element(By.TAG_NAME, 'h2')  ## select a locator for text on top of page
        if "Appointment Confirmation" in self.driver.page_source:
            print(" Appointment is scheduled with zero when it shouldn't have been.")
            # Go back manually to the appointment page so test_007 can continue
            self.driver.find_element(By.XPATH,"//a[normalize-space()='Go to Homepage']").click()
            pytest.fail("Appointment should not be scheduled with invalid input zero but it did with zeros.")
        else:
            print(" Invalid appointment was correctly rejected.")

    @pytest.mark.regression
    @pytest.mark.order(7)
    @pytest.mark.dependency(depends=["valid_login"])
    def test_007_valid_appointment_scheduling(self):
        appointment = AppointmentPage(self.driver, self.wait)
        self.driver.refresh()  ## need to reload
        appointment.click_facility_dropdown() ## Selecting
        time.sleep(4)
        appointment.select_apply_for_hospital_readmission_checkmark() ## checking the check mark
        appointment.click_medicare_radio_button() ### selecting the radio button
        appointment.calendar("08/04/2025")
        appointment.write_in_comment_box("hello my name is tino i would like to schedule an appointment")
        time.sleep(4)
        appointment.click_book_appointment()
        time.sleep(5)
        h2_tag_8 = self.driver.find_element(By.TAG_NAME, 'h2') ## after valid scheduling Appointment Confirmation
        assert h2_tag_8.text == "Appointment Confirmation", f"expected 'Appointment Confirmation' but got {h2_tag_8.text}" ## making sure we the test pass
        redirect = self.driver.find_element(By.XPATH,"//a[normalize-space()='Go to Homepage']") ## got to home element
        redirect.click() ##





















