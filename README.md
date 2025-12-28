# End-to-End QA Pipeline

**Senior QA Automation Engineer Portfolio Project**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green)](https://www.selenium.dev/)
[![Postman/Newman](https://img.shields.io/badge/Postman-Newman-orange)](https://www.postman.com/)
[![Allure Reports](https://img.shields.io/badge/Reports-Allure-brightgreen)](https://allurereport.org/)
[![JIRA Integration](https://img.shields.io/badge/JIRA-Auto%20Bug%20Logging-ff9900)](https://www.atlassian.com/software/jira)

A complete **one-command End-to-End QA automation pipeline** that validates both UI and API layers, generates rich reports, and automatically creates JIRA tickets on test failures.

Perfect demonstration of modern QA engineering skills: test orchestration, reporting, defect management, and secure configuration.

## Features

- **UI Automation** — Selenium with Page Object Model (POM) for maintainable tests
- **API Testing** — Postman collections executed via Newman (CLI) for load and functional validation
- **Orchestration** — Single Python script (`pipeline.py`) runs everything sequentially
- **Reporting** — Comprehensive Allure reports with screenshots and logs
- **Automatic Defect Logging** — Creates JIRA issues with details on any failure
- **Secure Configuration** — Credentials and URLs stored in `.env` (never hardcoded)
- **Screenshots on Failure** — Automatic captures saved for debugging

## Architecture Overview

The pipeline works as follows:

1. `pipeline.py` triggers UI tests (Selenium with POM)
2. `pipeline.py` triggers API tests (Newman/Postman collections)
3. Test results are collected and used to generate Allure reports
4. If any test fails → `jira_integration.py` automatically creates a JIRA ticket with details and attachments
5. On UI test failures → screenshots are saved to `screenshots/`

### Example Pipeline Architecture Diagrams

![QA Pipeline Architecture Example 1](https://www.testim.io/wp-content/uploads/2022/08/CI-CD-Pipeline.png)
![QA Pipeline Architecture Example 2](https://www.browserstack.com/guide/wp-content/uploads/2023/05/CI-CD-Pipeline.png)
![QA Pipeline Architecture Example 3](https://miro.medium.com/v2/resize:fit:1400/1*9pT9oq9n2v0f0b8f0b8f0b8f0b8f0b8f0b8f.png)

## Project Structure
.
├── api_tests/            # Postman collections & Newman scripts
├── ui_tests/             # Selenium tests (Page Object Model)
├── reports/              # Generated Allure/HTML reports
├── screenshots/          # Screenshots from failed UI tests (renamed for correctness)
├── jira_integration.py   # JIRA bug creation logic
├── pipeline.py           # Main orchestrator script
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (gitignored)
└── README.md


## Quick Start

### 1. Prerequisites
- Python 3.10+
- Node.js (for Newman)
- Chrome browser + ChromeDriver (managed via WebDriver Manager)

### 2. Setup
git clone https://github.com/AlekseiIvanovI/end-to-end-qa-pipeline.git
cd end-to-end-qa-pipeline

# Install dependencies
pip install -r requirements.txt

# Install Newman globally (if not already)
npm install -g newman
npm install -g newman-reporter-allure

3. Configuration
Create a .env file in the root directory:
BASE_URL=https://example.com                # Application URL
JIRA_BASE_URL=https://your-company.atlassian.net
JIRA_PROJECT_KEY=QA
JIRA_API_TOKEN=your_jira_api_token_here
JIRA_USER_EMAIL=your.email@example.com
Security Note: .env is included in .gitignore — never commit credentials!

4. Run the Pipeline
python pipeline.py

The script will:

Execute UI tests (Selenium)
Execute API tests (Newman)
Generate reports in reports/
Create JIRA tickets automatically if any test fails

5. View Reports
After execution:
allure serve reports/
(This opens an interactive Allure report in your browser with screenshots, logs, and trends.)

Technologies Used

Python — Orchestration and utilities
Selenium WebDriver — UI automation
pytest — Test framework
Postman + Newman — API testing
Allure — Advanced reporting
JIRA REST API — Automated bug logging
python-dotenv — Secure env management

Author
Aleksei Ivanov
Senior QA Automation Engineer (7+ years experience)
GitHub Profile | LinkedIn (add your LinkedIn link here)

Note: This is a portfolio demonstration project. Real-world company contributions are on private repositories.
Feel free to star ⭐ the repo if you find it useful!
