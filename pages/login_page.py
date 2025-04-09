from selenium.webdriver.common.by import By

from pages.home_page import HomePage  # if using menu actions

class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.home_page = HomePage(driver, wait)


    def click_username_field(self,username_value):
        username = self.driver.find_element(By.ID, 'txt-username') # locator with username field
        username.send_keys(username_value)

    def click_password_field(self, password_value):
        password =  self.driver.find_element(By.ID, 'txt-password')  # Locator with password field
        password.send_keys(password_value)


    def click_login_button(self):
        button = self.driver.find_element(By.ID, 'btn-login') # locator with login button
        button.click()


    ### submenu on  page is the same on the login page
    def use_menu_to_login(self):
        self.home_page.click_menu_and_login()


