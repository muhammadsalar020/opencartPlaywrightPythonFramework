# test_user_registration_data_driven.py
import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from utilities.data_reader_util import read_csv_data, read_json_data, read_excel_data
from utilities.random_data_util import RandomDataUtil

# ---------------------------------------------------------------------------
# Load test data from CSV, JSON, and Excel
# Columns/keys (in order): testName, firstName, lastName, email, password
# Note: email from CSV is IGNORED — a unique random email is generated each run
# ---------------------------------------------------------------------------
CSV_DATA   = read_csv_data("testdata/registrationdata.csv")
# JSON_DATA  = read_json_data("testdata/registrationdata.json")
# EXCEL_DATA = read_excel_data("testdata/registrationdata.xlsx")


# ---------------------------------------------------------------------------
# Helper: shared registration logic
# ---------------------------------------------------------------------------
def _perform_registration(page, test_name, first_name, last_name, password, source):
    home_page         = HomePage(page)
    registration_page = RegistrationPage(page)

    # --- Generate unique email every run ---
    random_data  = RandomDataUtil()
    unique_email = random_data.get_email()

    # --- Step 1: Navigate to Registration Page ---
    home_page.click_my_account()
    home_page.click_register()

    # --- Step 2: Fill Registration Form ---
    registration_page.set_first_name(first_name)
    registration_page.set_last_name(last_name)
    registration_page.set_email(unique_email)       # ← always a fresh unique email
    registration_page.set_password(password)
    registration_page.set_privacy_policy()
    registration_page.click_continue()

    # --- Step 3: Verify Registration Success ---
    expect(registration_page.get_confirmation_msg()).to_be_visible(timeout=5000), \
        f"[{source}][{test_name}] Registration failed: Confirmation message not displayed."

    print(f"[{source}][{test_name}] Registered with email: {unique_email}")


# ---------------------------------------------------------------------------
# Test 1: Data from CSV  ✅ ACTIVE
# ---------------------------------------------------------------------------
@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.parametrize(
    "test_name, first_name, last_name, email, password",
    CSV_DATA,
    ids=[row[0] for row in CSV_DATA]
)
def test_user_registration_csv(page, test_name, first_name, last_name, email, password):
    """Data-Driven Registration — source: testdata/registrationdata.csv
    Note: email column from CSV is ignored — unique email generated per run.
    """
    _perform_registration(page, test_name, first_name, last_name, password, source="CSV")


# ---------------------------------------------------------------------------
# Test 2: Data from JSON  ⏸ COMMENTED — uncomment when registrationdata.json is ready
# ---------------------------------------------------------------------------
# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.parametrize(
#     "test_name, first_name, last_name, email, password",
#     JSON_DATA,
#     ids=[row[0] for row in JSON_DATA]
# )
# def test_user_registration_json(page, test_name, first_name, last_name, email, password):
#     """Data-Driven Registration — source: testdata/registrationdata.json"""
#     _perform_registration(page, test_name, first_name, last_name, password, source="JSON")


# ---------------------------------------------------------------------------
# Test 3: Data from Excel  ⏸ COMMENTED — uncomment when registrationdata.xlsx is ready
# ---------------------------------------------------------------------------
# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.parametrize(
#     "test_name, first_name, last_name, email, password",
#     EXCEL_DATA,
#     ids=[row[0] for row in EXCEL_DATA]
# )
# def test_user_registration_excel(page, test_name, first_name, last_name, email, password):
#     """Data-Driven Registration — source: testdata/registrationdata.xlsx"""
#     _perform_registration(page, test_name, first_name, last_name, password, source="Excel")



# # test_user_registration_data_driven.py
# import pytest
# from playwright.sync_api import expect
# from pages.home_page import HomePage
# from pages.registration_page import RegistrationPage
# from utilities.data_reader_util import read_csv_data, read_json_data, read_excel_data
#
# # ---------------------------------------------------------------------------
# # Load test data from CSV, JSON, and Excel
# # Columns/keys (in order): testName, firstName, lastName, email, password
# # ---------------------------------------------------------------------------
# CSV_DATA   = read_csv_data("testdata/registrationdata.csv")
# # JSON_DATA  = read_json_data("testdata/registrationdata.json")
# # EXCEL_DATA = read_excel_data("testdata/registrationdata.xlsx")
#
#
# # ---------------------------------------------------------------------------
# # Helper: shared registration logic
# # ---------------------------------------------------------------------------
# def _perform_registration(page, test_name, first_name, last_name, email, password, source):
#     home_page         = HomePage(page)
#     registration_page = RegistrationPage(page)
#
#     # --- Step 1: Navigate to Registration Page ---
#     home_page.click_my_account()
#     home_page.click_register()
#
#     # --- Step 2: Fill Registration Form ---
#     registration_page.set_first_name(first_name)
#     registration_page.set_last_name(last_name)
#     registration_page.set_email(email)
#     registration_page.set_password(password)
#     registration_page.set_privacy_policy()
#     registration_page.click_continue()
#
#     # --- Step 3: Verify Registration Success ---
#     expect(registration_page.get_confirmation_msg()).to_be_visible(timeout=5000), \
#         f"[{source}][{test_name}] Registration failed: Confirmation message not displayed."
#
#
# # ---------------------------------------------------------------------------
# # Test 1: Data from CSV  ✅ ACTIVE
# # ---------------------------------------------------------------------------
# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.parametrize(
#     "test_name, first_name, last_name, email, password",
#     CSV_DATA,
#     ids=[row[0] for row in CSV_DATA]
# )
# def test_user_registration_csv(page, test_name, first_name, last_name, email, password):
#     """Data-Driven Registration — source: testdata/registrationdata.csv"""
#     _perform_registration(page, test_name, first_name, last_name, email, password, source="CSV")
#

# ---------------------------------------------------------------------------
# Test 2: Data from JSON  ⏸ COMMENTED — uncomment when registrationdata.json is ready
# ---------------------------------------------------------------------------
# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.parametrize(
#     "test_name, first_name, last_name, email, password",
#     JSON_DATA,
#     ids=[row[0] for row in JSON_DATA]
# )
# def test_user_registration_json(page, test_name, first_name, last_name, email, password):
#     """Data-Driven Registration — source: testdata/registrationdata.json"""
#     _perform_registration(page, test_name, first_name, last_name, email, password, source="JSON")


# ---------------------------------------------------------------------------
# Test 3: Data from Excel  ⏸ COMMENTED — uncomment when registrationdata.xlsx is ready
# ---------------------------------------------------------------------------
# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.parametrize(
#     "test_name, first_name, last_name, email, password",
#     EXCEL_DATA,
#     ids=[row[0] for row in EXCEL_DATA]
# )
# def test_user_registration_excel(page, test_name, first_name, last_name, email, password):
#     """Data-Driven Registration — source: testdata/registrationdata.xlsx"""
#     _perform_registration(page, test_name, first_name, last_name, email, password, source="Excel")