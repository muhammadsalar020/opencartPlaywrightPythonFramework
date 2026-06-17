import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from config import Config


@pytest.mark.sanity
@pytest.mark.regression
def test_product_search(page):
    """
    Test Case: Verify that searching for a valid product returns relevant results.

    Steps:
        1. Open the application in the browser.
        2. Locate the search box on the Home page.
        3. Enter a valid product name from Config in the search box.
        4. Click the Search button.
        5. Verify the Search Results page is displayed.
        6. Verify the searched product appears in the results list.

    Expected Result:
        The Search Results page is displayed and the searched product
        is visible in the search results list.
    """

    # --- Page Object Initialization ---
    home_page           = HomePage(page)
    search_results_page = SearchResultsPage(page)

    # --- Step 3: Enter product name from Config ---
    home_page.enter_search_text(Config.product_name)

    # --- Step 4: Click the Search button ---
    home_page.click_search_button()

    # --- Step 5: Verify Search Results page is displayed ---
    expect(search_results_page.get_search_results_heading()).to_be_visible(timeout=5000)

    # --- Step 6: Verify the searched product appears in the results ---
    expect(search_results_page.get_product_by_name(Config.product_name)).to_be_visible(timeout=5000)


# import pytest
# from playwright.sync_api import expect
# from pages.home_page import HomePage
# from pages.search_results_page import SearchResultsPage
#
#
# @pytest.mark.sanity
# @pytest.mark.regression
# def test_product_search(page):
#     """
#     Test Case: Verify that searching for a valid product returns relevant results.
#
#     Steps:
#         1. Open the application in the browser.
#         2. Locate the search box on the Home page.
#         3. Enter a valid product name ("iPhone") in the search box.
#         4. Click the Search button.
#         5. Verify the Search Results page is displayed.
#         6. Verify the searched product appears in the results list.
#
#     Expected Result:
#         The Search Results page is displayed and the searched product
#         is visible in the search results list.
#     """
#
#     # --- Page Object Initialization ---
#     home_page           = HomePage(page)
#     search_results_page = SearchResultsPage(page)
#
#     # --- Step 3: Enter product name in the search box ---
#     home_page.enter_search_text("iPhone")
#
#     # --- Step 4: Click the Search button ---
#     home_page.click_search_button()
#
#     # --- Step 5: Verify Search Results page is displayed ---
#     expect(search_results_page.get_search_results_heading()).to_be_visible(timeout=5000)
#
#     # --- Step 6: Verify the searched product appears in the results ---
#     expect(search_results_page.get_product_by_name("iPhone")).to_be_visible(timeout=5000)


# """
# Test Case: Product Search Functionality
#
# ===========================================
# Test Steps
# ===========================================
#
# 1. Open the application in the browser.
# 2. Locate the search box on the Home page.
# 3. Enter a valid product name (for example, "iPhone") in the search box.
# 4. Click on the "Search" button.
# 5. Verify that the Search Results page is displayed.
# 6. Check if the searched product name appears in the list of search results.
#
# Expected Result:
# ----------------
# The Search Results page should appear, and the searched product should be
# visible in the search results list.
# """
# import pytest
# from playwright.sync_api import expect
# from pages.home_page import HomePage
# from pages.search_results_page import SearchResultsPage
# from config import Config
#
# @pytest.mark.sanity
# @pytest.mark.regression
# def test_product_search(page):
#
#     product_name=Config.product_name
#
#     home_page = HomePage(page)
#     search_results_page = SearchResultsPage(page)
#
#
#     home_page.enter_product_name(product_name)
#     home_page.click_search()
#
#     expect(search_results_page.get_search_results_page_header()).to_be_visible(timeout=3000)
#     expect(search_results_page.is_product_exist(product_name)).to_be_visible(timeout=3000)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
