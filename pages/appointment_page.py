


from pages.submenu import SubMenu  # import submenu if in another file


class AppointmentPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.submenu = SubMenu(driver, wait)  # initialize submenu here

    def click_facility_dropdown(self):
        pass

    def select_apply_for_hospital_readmission_checkmark(self):
        pass

    def click_medicare_radio_button(self):
        pass

    def click_medicaid_button(self):
        pass

    def click_none(self):
        pass

    def calendar(self):
        pass

    def write_in_comment_box(self):
        pass

    def click_book_appointment(self):
        pass

    # You can call submenu actions like this:
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

