import pytest
import requests
from TBL.urls import urls

from TBL.critical_pages import CriticalPages

class TestMainPages(CriticalPages):

    @pytest.mark.parametrize("page, url", urls)
    def test_page_loads(self, page, url):
        #Check HTTP status codes using requests
        response = requests.get(url)
        assert response.status_code == 200, f"{page} did not return a 200 status code"

        # Then confirm the page loads properly using Selenium
        self.driver.get(url)
        assert self.driver.title != "", f"{page} did not load properly"

