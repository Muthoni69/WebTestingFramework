# Web Testing Automation Project

This project contains automated tests for a website using **Selenium**, **pytest**, and **Python**. The main focus is on testing the responsiveness of the website on different screen sizes, verifying that critical pages load correctly, and ensuring there are no broken links across the site.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Test Cases](#test-cases)
- [Project Setup](#project-setup)
- [Running Tests](#running-tests)
  - [Responsiveness Testing](#responsiveness-testing)
  - [Broken Links Testing](#broken-links-testing)
  - [Generating Test Reports](#generating-test-reports)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)

---

## Project Overview

This project automates key functionality tests of a website. The test suite checks for:
1. **Responsiveness**: Ensures the website behaves correctly on desktop, tablet, and mobile screen sizes.
2. **Critical Pages**: Verifies that important pages return a 200 status code and load properly.
3. **Broken Links**: Checks all links on the website to ensure none are broken.

## Technologies Used

- **Python**: Main programming language.
- **Selenium**: Browser automation tool.
- **pytest**: Testing framework.
- **pytest-html**: For generating detailed HTML reports.
- **WebDriver Manager**: Manages browser drivers (Chrome, Firefox, Edge).

## Test Cases

### 1. Responsive Design Testing
Tests the website's behavior on different screen sizes:
- Desktop (1920x1080)
- Tablet (1280x800)
- Mobile (375x667)

### 2. Critical Pages Testing
Ensures important pages (like "Engineering", "Solutions", "Cloud Services") load correctly and return the expected HTTP status codes.

### 3. Broken Links Testing
Verifies that all links on the site are valid and no 404 (Not Found) errors occur.

## Project Setup

### Prerequisites
Make sure you have the following installed:
- Python 3.x
- pip (Python package manager)
- Google Chrome, Firefox, or Microsoft Edge

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/web-testing-automation.git
    cd web-testing-automation
    ```

2. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Add browser drivers (Chrome, Firefox, or Edge) to your system PATH or let WebDriver Manager handle them.

## Running Tests

### 1. Responsiveness Testing

To test how the website behaves across different screen sizes:
```bash
pytest tests/test_responsive_design.py --browser chrome
```

The screen sizes tested include:
- Desktop: 1920x1080
- Tablet: 1280x800
- Mobile: 375x667

### 2. Broken Links Testing

To test for broken links:
```bash
pytest tests/test_broken_links.py --browser chrome
```

This will check all the links on the website to ensure they are functioning.

### 3. Generating Test Reports

To generate an HTML report after running tests:
```bash
pytest tests/test_responsive_design.py --html=report.html --browser chrome
```

### Example: Running tests on a specific screen size (Mobile)
```bash
pytest tests/test_responsive_design.py --browser chrome -k "375, 667"
```

## Directory Structure

```bash
web-testing-automation/
│
├── tests/
│   ├── test_responsive_design.py      # Tests for responsiveness on different screen sizes
│   ├── test_broken_links.py           # Tests for broken links on the website
│   ├── test_critical_pages.py         # Verifies key pages are loading correctly
│
├── TBL/
│   ├── urls.py                        # Contains URLs for testing
│   ├── responsive_design.py           # Code for handling responsiveness test logic
│   ├── critical_pages.py              # Code for handling critical page tests
│   ├── broken_links.py                # Code for checking broken links
│
├── conftest.py                         # Configuration for pytest fixtures (browser, screen sizes)
├── pytest.ini                          # pytest configuration file
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
```

## Contributing

If you'd like to contribute to this project:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Push to your branch and create a pull request.

## License

This project is licensed under the MIT License.
