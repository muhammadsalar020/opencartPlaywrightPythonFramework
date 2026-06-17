# test_end_to_end.py
import pytest
import time
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.logout_page import LogoutPage
from utilities.random_data_util import RandomDataUtil
from config import Config

STEP_DELAY = 5  # seconds delay after each step


@pytest.mark.end_to_end
def test_end_to_end_user_journey(page):
    """
    E2E Test: Complete user journey —
    Register → Logout → Login → Search Product → Add to Cart → Logout
    """

    # =============================
    # STEP 1: Register a new account
    # =============================
    home_page         = HomePage(page)
    registration_page = RegistrationPage(page)
    my_account_page   = MyAccountPage(page)
    login_page        = LoginPage(page)
    search_results    = SearchResultsPage(page)
    product_page      = ProductPage(page)
    logout_page       = LogoutPage(page)

    home_page.click_my_account()
    home_page.click_register()

    random_data = RandomDataUtil()
    email    = random_data.get_email()
    password = random_data.get_password()

    registration_page.set_first_name(random_data.get_first_name())
    registration_page.set_last_name(random_data.get_last_name())
    registration_page.set_email(email)
    registration_page.set_password(password)
    registration_page.set_privacy_policy()
    registration_page.click_continue()

    expect(registration_page.get_confirmation_msg()).to_be_visible(timeout=5000)
    print(f"[STEP 1] Registered with email: {email}")
    time.sleep(STEP_DELAY)

    # =============================
    # STEP 2: Logout after registration
    # =============================
    my_account_page.click_logout()

    expect(logout_page.get_logout_page_heading()).to_be_visible(timeout=5000)
    logout_page.click_continue()

    expect(page).to_have_title("Your Store", timeout=5000)
    print("[STEP 2] Logged out after registration")
    time.sleep(STEP_DELAY)

    # =============================
    # STEP 3: Login with new account
    # =============================
    home_page.click_my_account()
    home_page.click_login()

    login_page.set_email(email)
    login_page.set_password(password)
    login_page.click_login()

    expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=5000)
    print("[STEP 3] Logged in successfully")
    time.sleep(STEP_DELAY)

    # =============================
    # STEP 4: Search for a product
    # =============================
    home_page.enter_product_name(Config.product_name)
    home_page.click_search()

    expect(search_results.get_search_results_heading()).to_be_visible(timeout=5000)
    expect(search_results.get_product_by_name(Config.product_name)).to_be_visible(timeout=5000)
    print(f"[STEP 4] Search results displayed for: {Config.product_name}")
    time.sleep(STEP_DELAY)

    # =============================
    # STEP 5: Add product to cart
    # =============================
    search_results.select_product(Config.product_name)

    product_page.set_quantity(Config.product_quantity)
    product_page.add_to_cart()

    expect(product_page.get_confirmation_message()).to_be_visible(timeout=5000)
    expect(product_page.get_confirmation_message()).to_contain_text(Config.product_name)
    print(f"[STEP 5] '{Config.product_name}' added to cart successfully")
    time.sleep(STEP_DELAY)

    # =============================
    # STEP 6: Logout
    # =============================
    my_account_page.click_logout()

    expect(logout_page.get_logout_page_heading()).to_be_visible(timeout=5000)
    logout_page.click_continue()

    expect(page).to_have_title("Your Store", timeout=5000)
    print("[STEP 6] Logged out successfully — E2E journey complete!")
    time.sleep(STEP_DELAY)

# # test_end_to_end.py
# import pytest
# from playwright.sync_api import expect
# from pages.home_page import HomePage
# from pages.registration_page import RegistrationPage
# from pages.login_page import LoginPage
# from pages.my_account_page import MyAccountPage
# from pages.search_results_page import SearchResultsPage
# from pages.product_page import ProductPage
# from pages.logout_page import LogoutPage
# from utilities.random_data_util import RandomDataUtil
# from config import Config
#
#
# @pytest.mark.end_to_end
# def test_end_to_end_user_journey(page):
#     """
#     E2E Test: Complete user journey —
#     Register → Logout → Login → Search Product → Add to Cart → Logout
#     """
#
#     # =============================
#     # STEP 1: Register a new account
#     # =============================
#     home_page         = HomePage(page)
#     registration_page = RegistrationPage(page)
#     my_account_page   = MyAccountPage(page)
#     login_page        = LoginPage(page)
#     search_results    = SearchResultsPage(page)
#     product_page      = ProductPage(page)
#     logout_page       = LogoutPage(page)
#
#     home_page.click_my_account()
#     home_page.click_register()
#
#     random_data = RandomDataUtil()
#     email    = random_data.get_email()
#     password = random_data.get_password()
#
#     registration_page.set_first_name(random_data.get_first_name())
#     registration_page.set_last_name(random_data.get_last_name())
#     registration_page.set_email(email)
#     registration_page.set_password(password)
#     registration_page.set_privacy_policy()
#     registration_page.click_continue()
#
#     # Verify registration success
#     expect(registration_page.get_confirmation_msg()).to_be_visible(timeout=5000)
#     print(f"[STEP 1] Registered with email: {email}")
#
#     # =============================
#     # STEP 2: Logout after registration
#     # =============================
#     my_account_page.click_logout()
#
#     # Verify logout page is displayed
#     expect(logout_page.get_logout_page_heading()).to_be_visible(timeout=5000)
#     logout_page.click_continue()
#
#     # Verify redirected to Home page
#     expect(page).to_have_title("Your Store", timeout=5000)
#     print("[STEP 2] Logged out after registration")
#
#     # =============================
#     # STEP 3: Login with new account
#     # =============================
#     home_page.click_my_account()
#     home_page.click_login()
#
#     login_page.set_email(email)
#     login_page.set_password(password)
#     login_page.click_login()
#
#     # Verify login success
#     expect(my_account_page.get_my_account_page_heading()).to_be_visible(timeout=5000)
#     print("[STEP 3] Logged in successfully")
#
#     # =============================
#     # STEP 4: Search for a product
#     # =============================
#     home_page.enter_product_name(Config.product_name)
#     home_page.click_search()
#
#     # Verify search results
#     expect(search_results.get_search_results_heading()).to_be_visible(timeout=5000)
#     expect(search_results.get_product_by_name(Config.product_name)).to_be_visible(timeout=5000)
#     print(f"[STEP 4] Search results displayed for: {Config.product_name}")
#
#     # =============================
#     # STEP 5: Add product to cart
#     # =============================
#     search_results.select_product(Config.product_name)
#
#     product_page.set_quantity(Config.product_quantity)
#     product_page.add_to_cart()
#
#     # Verify success confirmation message
#     expect(product_page.get_confirmation_message()).to_be_visible(timeout=5000)
#     expect(product_page.get_confirmation_message()).to_contain_text(Config.product_name)
#     print(f"[STEP 5] '{Config.product_name}' added to cart successfully")
#
#     # =============================
#     # STEP 6: Logout
#     # =============================
#     my_account_page.click_logout()
#
#     # Verify logout page
#     expect(logout_page.get_logout_page_heading()).to_be_visible(timeout=5000)
#     logout_page.click_continue()
#
#     # Verify redirected to Home page
#     expect(page).to_have_title("Your Store", timeout=5000)
#     print("[STEP 6] Logged out successfully — E2E journey complete!")