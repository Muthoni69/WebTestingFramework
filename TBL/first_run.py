import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

#Setup and Basic Functionality
class TestBrowser:

    # Define a fixture for browser setup
    #The browser fixture is parameterized with "chrome", "firefox", and "edge".
    @pytest.fixture(params=["chrome", "firefox", "edge"], scope="class")
    def browser(self, request):
        if request.param == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()),
                                      options=options)

        elif request.param == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            driver = webdriver.Firefox(service=webdriver.firefox.service.Service(GeckoDriverManager().install()), options=options)

        elif request.param == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            driver = webdriver.Edge(service=webdriver.edge.service.Service(EdgeChromiumDriverManager().install()), options=options)

        yield driver
        #yield driver, request.param #The 'yield' driver provides driver to the test
        driver.maximize_window()
        driver.quit()



