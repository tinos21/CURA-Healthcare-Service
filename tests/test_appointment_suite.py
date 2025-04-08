

import time

import pytest
from selenium.webdriver.common.by import By


from pages.home_page import HomePage
from pages.login_page import LoginPage
## combo_facility

pytest.mark.usefixtures("setup_driver")
class TestAppoinmentSuite:

