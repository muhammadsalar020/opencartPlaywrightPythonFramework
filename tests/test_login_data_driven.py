import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from utilities.data_reader_util import read_csv_data, read_json_data, read_excel_data

# ---------------------------------------------------------------------------
# Load test data from CSV, JSON, and Excel
# Columns/keys (in order): testName, email, password, expected
# ---------------------------------------------------------------------------
# CSV_DATA   = read_csv_data("testdata/logindata.csv")
# JSON_DATA  = read_json_data("testdata/logindata.json")
EXCEL_DATA = read_excel_data("testdata/logindata.xlsx")


# ---------------------------------------------------------------------------
# Helper: shared login logic
# ---------------------------------------------------------------------------
def _perform_login(page, test_name, email, password, expected, source):
    home_page       = HomePage(page)
    login_page      = LoginPage(page)
    my_account_page = MyAccountPage(page)

    # --- Step 1: Navigate to Login Page ---
    home_page.click_my_account()
    home_page.click_login()

    # --- Step 2: Enter Credentials ---
    login_page.set_email(email)
    login_page.set_password(password)

    # --- Step 3: Submit & Assert ---
    if expected == "success":
        login_page.click_login()
        expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=5000), \
            f"[{source}][{test_name}] Expected 'My Account' heading to be visible after successful login."

    elif expected == "failure":
        login_page.click_login_no_nav()
        expect(login_page.get_login_error()).to_be_visible(timeout=5000), \
            f"[{source}][{test_name}] Expected login error to be visible for invalid credentials."

    else:
        pytest.fail(
            f"[{source}][{test_name}] Unknown 'expected' value '{expected}'. "
            "Use 'success' or 'failure'."
        )


# ---------------------------------------------------------------------------
# Test 1: Data from CSV  ✅ ACTIVE
# ---------------------------------------------------------------------------
# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.parametrize(
#     "test_name, email, password, expected",
#     CSV_DATA if CSV_DATA else [("no_data", "", "", "skip")],
#     ids=[row[0] for row in CSV_DATA] if CSV_DATA else ["no_data"]
# )
# def test_login_data_driven_csv(page, test_name, email, password, expected):
#     """Data-Driven Login — source: testdata/logindata.csv"""
#     if expected == "skip":
#         pytest.skip("No CSV data found in testdata/logindata.csv")
#     _perform_login(page, test_name, email, password, expected, source="CSV")


# ---------------------------------------------------------------------------
# Test 2: Data from JSON  ⏸ COMMENTED — uncomment when logindata.json is ready
# ---------------------------------------------------------------------------
# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.parametrize(
#     "test_name, email, password, expected",
#     JSON_DATA if JSON_DATA else [("no_data", "", "", "skip")],
#     ids=[row[0] for row in JSON_DATA] if JSON_DATA else ["no_data"]
# )
# def test_login_data_driven_json(page, test_name, email, password, expected):
#     """Data-Driven Login — source: testdata/logindata.json"""
#     if expected == "skip":
#         pytest.skip("No JSON data found in testdata/logindata.json")
#     _perform_login(page, test_name, email, password, expected, source="JSON")
#

# ---------------------------------------------------------------------------
# Test 3: Data from Excel  ⏸ COMMENTED — uncomment when logindata.xlsx is ready
# ---------------------------------------------------------------------------
@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.parametrize(
    "test_name, email, password, expected",
    EXCEL_DATA if EXCEL_DATA else [("no_data", "", "", "skip")],
    ids=[row[0] for row in EXCEL_DATA] if EXCEL_DATA else ["no_data"]
)
def test_login_data_driven_excel(page, test_name, email, password, expected):
    """Data-Driven Login — source: testdata/logindata.xlsx"""
    if expected == "skip":
        pytest.skip("No Excel data found in testdata/logindata.xlsx")
    _perform_login(page, test_name, email, password, expected, source="Excel")

# import pytest
# from playwright.sync_api import expect
# from pages.home_page import HomePage
# from pages.login_page import LoginPage
# from pages.my_account_page import MyAccountPage
# from utilities.data_reader_util import read_csv_data
#
# # ---------------------------------------------------------------------------
# # Load test data from CSV
# # CSV columns (in order): testName, email, password, expected
# # ---------------------------------------------------------------------------
# LOGIN_TEST_DATA = read_csv_data("testdata/logindata.csv")
#
#
# def pytest_ids(val):
#     """Use the testName column (first element) as the readable test ID."""
#     return val[0]
#
#
# # ---------------------------------------------------------------------------
# # Data-Driven Tests
# # ---------------------------------------------------------------------------
#
# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.parametrize("test_name, email, password, expected", LOGIN_TEST_DATA, ids=pytest_ids)
# def test_login_data_driven(page, test_name, email, password, expected):
#     """
#     Data-Driven Test Case: Verify login behaviour for multiple credential sets.
#
#     Test data is read from:  testdata/logindata.csv
#     CSV columns             : testName, email, password, expected
#     Expected values         : 'success'  → login should succeed
#                               'failure'  → login should fail with an error message
#     """
#
#     # --- Page Object Initialization ---
#     home_page = HomePage(page)
#     login_page = LoginPage(page)
#     my_account_page = MyAccountPage(page)
#
#     # --- Step 1: Navigate to Login Page ---
#     home_page.click_my_account()
#     home_page.click_login()
#
#     # --- Step 2: Enter Credentials ---
#     login_page.set_email(email)
#     login_page.set_password(password)
#
#     # --- Step 3: Submit & Assert ---
#     if expected == "success":
#         # Valid login → navigates away from login page
#         login_page.click_login()
#         expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=5000), \
#             f"[{test_name}] Expected 'My Account' heading to be visible after successful login."
#
#     elif expected == "failure":
#         # Invalid login → stays on login page, error should appear
#         login_page.click_login_no_nav()
#         expect(login_page.get_login_error()).to_be_visible(timeout=5000), \
#             f"[{test_name}] Expected login error to be visible for invalid credentials."
#
#     else:
#         pytest.fail(
#             f"[{test_name}] Unknown 'expected' value '{expected}' in CSV. "
#             "Use 'success' or 'failure'."
#         )