import pytest
from selenium import webdriver

from TBL.first_run import TestBrowser

@pytest.mark.usefixtures("browser", "screen_size")
class ResponsiveDesign(TestBrowser):

    @pytest.fixture(autouse=True)
    def set_driver(self, browser, screen_size): #This receives both the browser and screen_size
        self.driver = browser

        # Set window size according to screen size (Desktop, Tablet, Mobile)
        self.driver.set_window_size(screen_size[0], screen_size[1])  #width, height



