import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from TBL.broken_links import BrokenLinkChecker
from TBL.critical_pages import CriticalPages   #inherit from this to use the webdriver setup

class TestBrokenLinks(CriticalPages):
    def test_broken_links(self, browser):

        self.driver.get("http://65.2.33.17/engineering")

        #Find all the anchor tags(with the href)
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        broken_links = []

        for link in links:
            url = link.get_attribute('href')
            if url:
                status_code = BrokenLinkChecker.check_link(url)
                if status_code != 200:
                    broken_links.append((url, status_code))

        assert not broken_links, f"Broken links found: {broken_links}"


#pytest tests/test_broken_links.py --browser chrome
#pytest tests/test_broken_links.py --browser chrome --html=brokenlinks_report.html --self-contained-html

#pytest tests/test_broken_links.py --html=report.html --capture=tee-sys



