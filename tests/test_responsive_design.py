from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from TBL.responsive_design import ResponsiveDesign

class TestScreenSize(ResponsiveDesign):
    def test_responsiveness(self, screen_size):
        self.driver.get("http://65.2.33.17/")

        wait = WebDriverWait(self.driver, 20)

        try:
            #Try locating the dropdown to see if it exists
            dropdown_button = wait.until(
                EC.presence_of_element_located((By.XPATH, '//button[@data-bs-toggle="collapse"]')))

            # If dropdown button is found, click it to reveal the menu
            dropdown_button.click()
        except:
            # If the dropdown button is not present, it means the screen is large enough to show the menu without it
            pass


        # Now check if the engineering element is displayed
        engineering_element = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Engineering")))
        assert engineering_element.is_displayed(),  f"Engineering segment is not displayed at size {screen_size}"

#TRY RUNNING THE CODE FOR ONLY SMALL SIZE