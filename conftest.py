from email.policy import default

import pytest

def pytest_addoption(parser): #This function adds the --browser option to the pytest command-line arguments>>>pytest --browser chrome
    parser.addoption("--browser", action="store", default = "chrome",  help="Choose browser: chrome, firefox, or edge")

#Fixture for browser choice
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

# # Conditional fixture to apply screen size only if explicitly mentioned
# @pytest.fixture(autouse=True)
# def conditional_screen_size(request, screen_size):
#     if "screen_size" in request.fixturenames:  # Only inject screen_size if it's explicitly needed
#         request.getfixturevalue("screen_size")
#
# #Fixture for different screen sizes
# @pytest.fixture(params=[(1920, 1080), (1280, 800), (375, 667)]) # Desktop, Tablet, Mobile
# def screen_size(request):
#     return request.param

