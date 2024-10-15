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
- [Findings For Responsiveness](#response)
- [Findings For Brokenlinks](#broken-links)

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


### **Website Responsiveness Testing Report**

**Test Name:** Responsive Design Testing  
**URL Tested:** http://65.2.33.17/  
**Test Duration:** 1 minute 39 seconds

---

**Overall Results:**
- **Total Tests:** 6
- **Passed:** 4
- **Failed:** 2

---

#### **Test Details:**

1. **Chrome Browser (1920x1080) - Desktop View**
   - **Result:** PASSED  
   - **Time Taken:** 32.58 seconds  
   - **Description:** The website's responsiveness at a desktop resolution (1920x1080) was successfully tested. All elements, including the Engineering menu, were displayed correctly.

2. **Chrome Browser (1280x800) - Tablet View**
   - **Result:** PASSED  
   - **Time Taken:** 714 ms  
   - **Description:** The Engineering menu and other elements were successfully displayed at tablet resolution (1280x800).

3. **Chrome Browser (375x667) - Mobile View**
   - **Result:** FAILED  
   - **Time Taken:** 21.98 seconds  
   - **Error:** `TimeoutException: Unable to locate the "Engineering" link element`.  
   - **Issue Identified:** On mobile view, the dropdown menu needs to be manually triggered. The Engineering link was not found after attempting to interact with the dropdown button.

4. **Firefox Browser (1920x1080) - Desktop View**
   - **Result:** PASSED  
   - **Time Taken:** 11.57 seconds  
   - **Description:** Responsiveness at desktop resolution (1920x1080) passed successfully on Firefox.

5. **Firefox Browser (1280x800) - Tablet View**
   - **Result:** PASSED  
   - **Time Taken:** 796 ms  
   - **Description:** Tablet view passed without issues. All elements, including the Engineering link, were displayed correctly.

6. **Firefox Browser (375x667) - Mobile View**
   - **Result:** FAILED  
   - **Time Taken:** 21.87 seconds  
   - **Error:** `TimeoutException: Unable to locate the "Engineering" link element`.  
   - **Issue Identified:** Similar to Chrome, the dropdown menu was not functioning correctly on mobile view, preventing the Engineering link from being accessed.

---

### **Key Observations:**
- The website works well in both desktop and tablet views on Chrome and Firefox.
- Mobile view (375x667) failed in both browsers due to issues with the dropdown menu not being clicked or loaded properly, which blocked access to certain elements like the "Engineering" link.

### **Action Points:**
- Investigate the dropdown functionality at smaller screen sizes to ensure the navigation menu behaves as expected.
- Consider adding explicit waits or a more robust method to detect and interact with mobile dropdowns.

**This report highlights the success in larger screen sizes but identifies clear issues in mobile responsiveness that need further investigation and fixes.**

### Broken Links Test Report

A test was performed to identify broken links on the website using Selenium and pytest. The test ran on multiple browsers (Chrome, Firefox, and Edge) with the following results:

- **Test Duration**: 3 minutes and 31 seconds.
- **Browsers Tested**: Chrome, Firefox, Edge.

#### Failed Tests:

- **Chrome: Failed**
  - **Duration**: 1 minute and 41 seconds
  - **Broken Links**:
    - `tel:+1 3028930609` (Status: None)
    - `tel:+254738770186` (Status: None)
    - `tel:+254734770187` (Status: None)
    - `mailto:info@technobraingroup.com` (Status: None)
    - `https://www.linkedin.com/company/techno-brain-limited/` (Status: 999)
    - `https://twitter.com/TechnoBrainLtd/` (Status: 403)

- **Firefox: Failed**
  - **Duration**: 52.54 seconds
  - **Broken Links** (same as above)

- **Edge: Failed**
  - **Duration**: 57.51 seconds
  - **Broken Links** (same as above)

**These results highlight the need to address the detected broken links to improve the website's functionality.**

