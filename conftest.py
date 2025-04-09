import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


@pytest.fixture(scope="class")
def setup_driver(request):
    # Path to chromedriver
    chromedriver_path = ChromeDriverManager().install() ### this automatically install the latest chrome driver
    # Initialize the Chrome WebDriver service
    service = Service(executable_path=chromedriver_path)

    # Chrome options
    options = Options()
    options.add_argument("--incognito")
    # options.add_argument("--headless") we are not using jenkins yet
    ## options.add_argument("--headless")


    # Initialize WebDriver with the service object and options
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 15)


    #### https://ebay.com
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(3)
    driver.maximize_window() ## expand the window

    # passing driver and wait to test classes inside tests package
    request.cls.driver = driver
    request.cls.wait = wait

    # test completes before closing the driver
    yield

    # Cleanup after the test is done
    time.sleep(1)
    driver.quit()  # Quit the driver at the end of the test
