import pytest
from TBL.first_run import TestBrowser


class TestLandingPage(TestBrowser):

    def test_website_title(self, browser):
        driver, browser_type = browser
        driver.get("http://65.2.33.17/")
        title = driver.title
        print(f"Browser: {browser_type}, Title: {title}")
        assert "Home | TechnoBrain" in title
