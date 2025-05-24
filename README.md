# Insider Website UI Test Automation

This project automates UI testing for the [Insider website](https://useinsider.com) using **Selenium WebDriver** and **Pytest**. It follows the **Page Object Model (POM)** design pattern to ensure clean and maintainable test code.

---

## 📌 Project Structure
        project/
        │
        ├── pages/
        │   └── homepage.py
        ├── tests/
        │   └── test_homepage.py
        ├── conftest.py       # Optional shared fixtures
        └── requirements.txt


---

## ✅ Features

- Open the Insider homepage and verify the page title
- Accept cookie consent (if present)
- Click the "Company" tab in the top navigation
- Verify the visibility of the "Careers" link

---

## 🛠️ Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (compatible with your Chrome version)

---

## 📦 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/insider-ui-tests.git
   cd insider-ui-tests

2. Create a virtual environment (optional but recommended):
   ```bash
    python -m venv venv
    source venv/bin/activate  
    # On Windows: venv\Scripts\activate ```

3. Install dependencies:
    ```pip install -r requirements.txt```
    
## 🧪 Running the Tests
- To run all tests:
 ```pytest tests/ ```
 - To run a specific test file: 
 ```pytest tests/test_homepage.py ```
 - To see detailed logs and output
 ```pytest -v -s ```

## 🧹 Teardown
- Each test automatically closes the browser instance after execution using a pytest fixture.

## 🚀 Future Improvements
- Integrate with Jenkins for CI/CD
- Add HTML report generation (e.g., with pytest-html)
-Extend tests for "Careers" page validation
Add tests for mobile responsiveness with Selenium Grid