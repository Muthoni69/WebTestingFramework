import  pytest
from TBL.first_run import TestBrowser

@pytest.mark.usefixtures("browser") #Automatically applies the fixture
class CriticalPages(TestBrowser):
    @pytest.fixture(autouse=True) #
    def set_driver(self, browser): #Will receive the driver from the browser fixture
        self.driver = browser #self.driver is now initialized with the browser driver









