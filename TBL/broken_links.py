import pytest
import requests
from selenium.webdriver.common.by import By

class BrokenLinkChecker:
    @staticmethod
    #The static method places the below utility function(logically related to class but doesn't need class/instance specific data

    def check_link(url): #This class takes a url, sends a head request and returns the HTTP status code
        try:
            response = requests.head(url, allow_redirects=True)
            return response.status_code

        except requests.exceptions.RequestException as e:
            return None

