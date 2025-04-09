from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.submenu import SubMenu


class AppointmentPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.submenu = SubMenu(driver, wait)  # including  submenu

    ### method for drop down
    def click_facility_dropdown(self):
        select_1 = self.driver.find_element(By.ID, "combo_facility")
        select = Select(select_1)
        select.select_by_visible_text("Hongkong CURA Healthcare Center")  # select Hongkong

    ### method for select check mark
    def select_apply_for_hospital_readmission_checkmark(self):
        checkbox = self.driver.find_element(By.ID,"chk_hospotal_readmission")
        print(checkbox)
        checkbox.click()


    ### method for medicare radio
    def click_medicare_radio_button(self):
        radio = self.driver.find_element(By.ID, "radio_program_medicare")
        radio.click()

    ### radio button for medicaid
    def click_medicaid_button(self):
        pass
    ### radio button for none
    def click_none(self):
        pass

    ## method to interact with calendar
    def calendar(self,date):
        calendar = self.driver.find_element(By.ID, "txt_visit_date")
        calendar.click()
        calendar.clear()
        calendar.send_keys(date) ## days/month/year 00/00/0000
        calendar.send_keys(Keys.ENTER)



    def write_in_comment_box(self,comments):
        comment = self.driver.find_element(By.ID, "txt_comment")
        comment.click()
        comment.send_keys(comments)

    def click_book_appointment(self):
        bookapp = self.driver.find_element(By.ID, "btn-book-appointment")
        bookapp.click()


    # submenu actions bellow
    def click_menu_and_go_home(self):
        self.submenu.click_hamburger_menu()
        self.submenu.click_home()

    def click_menu_and_logout(self):
        self.submenu.click_hamburger_menu()
        self.submenu.click_logout()

    def click_menu_and_view_history(self):
        self.submenu.click_hamburger_menu()
        self.submenu.click_history()

    def click_menu_and_view_profile_page(self):
        pass

