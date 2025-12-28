import subprocess
import os
from jira_integration import create_jira_bug

# Ensure reports folder exists
os.makedirs("reports", exist_ok=True)

# Paths for Allure
ALLURE_RESULTS_DIR = os.path.join("reports", "allure-results")
ALLURE_REPORT_DIR = os.path.join("reports", "allure-report")
os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)


def run_ui_tests():
    print("Running UI tests (Selenium POM)...")

    html_report_path = os.path.join("reports", "ui_test_report.html")

    # Run pytest with HTML report and Allure results
    result = subprocess.run(
        [
            "pytest",
            "ui_tests/tests/",
            "-v",
            f"--html={html_report_path}",
            "--self-contained-html",
            f"--alluredir={ALLURE_RESULTS_DIR}"
        ],
        capture_output=True,
        text=True
    )
    print(result.stdout)

    # Generate Allure report
    subprocess.run(
        ["allure", "generate", ALLURE_RESULTS_DIR, "-o", ALLURE_REPORT_DIR, "--clean"],
        check=True,
        shell=True
    )
    print(f"Pytest HTML report: {html_report_path}")
    print(f"Allure report generated: {ALLURE_REPORT_DIR}")

    # Create JIRA bug if UI tests failed
    if result.returncode != 0:
        print("UI tests failed — attempting to create JIRA bug")
        try:
            create_jira_bug("UI Test Failure", result.stdout[:500])
        except Exception as e:
            print(f"Failed to create JIRA bug: {e}")

    return result.returncode, html_report_path, ALLURE_REPORT_DIR


def run_api_tests():
    print("Running API tests (Newman)...")
    result = subprocess.run(
        ["newman", "run", "api_tests/newman/collection.json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8",
        errors="ignore",
        shell=True
    )
    output = result.stdout + "\n" + result.stderr
    print(output)
    api_code = 0 if result.returncode == 0 else 1
    return api_code, output


def main():
    print("END-TO-END QA PIPELINE STARTED")
    print("=" * 50)

    # Run tests
    ui_code, html_report, allure_dir = run_ui_tests()
    api_code, api_output = run_api_tests()

    # Create combined summary HTML
    summary_path = os.path.join("reports", "pipeline_summary.html")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("<html><head><title>Pipeline Summary</title></head><body>")
        f.write("<h1>End-to-End QA Pipeline Summary</h1>")

        # UI tests
        f.write(f"<h2>UI Tests: {'PASS' if ui_code == 0 else 'FAIL'}</h2>")
        f.write(f"<p>Pytest HTML report: <a href='{os.path.basename(html_report)}'>View Report</a></p>")
        f.write(f"<p>Allure report folder: {allure_dir}</p>")

        # API tests
        f.write(f"<h2>API Tests: {'PASS' if api_code == 0 else 'FAIL'}</h2>")
        f.write("<pre>" + api_output + "</pre>")

        # Overall summary
        f.write("<h2>Overall Pipeline Result:</h2>")
        if ui_code == 0 and api_code == 0:
            f.write("<p style='color:green;font-weight:bold;'>ALL TESTS PASSED — FULL PIPELINE SUCCESS</p>")
        else:
            f.write("<p style='color:red;font-weight:bold;'>PIPELINE COMPLETED WITH FAILURES — CHECK JIRA AND REPORTS</p>")

        f.write("</body></html>")

    print("=" * 50)
    print(f"Pipeline summary report generated: {summary_path}")


if __name__ == "__main__":
    main()
