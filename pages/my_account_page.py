# my_account_page.py
from playwright.sync_api import Page
from pages.logout_page import LogoutPage


class MyAccountPage:
    """Page Object Model class for the My Account Page."""

    def __init__(self, page: Page):
        self.page = page

        # ===== Locators =====
        self.msg_heading       = page.locator('h1:has-text("My Account")')
        self.lnk_my_account    = page.locator('span:has-text("My Account")')
        self.lnk_logout        = page.locator("a.dropdown-item[href*='logout']")

    # ===== Page Validation Methods =====

    def get_my_account_page_heading(self):
        """Return the My Account page heading locator."""
        try:
            return self.msg_heading
        except Exception as e:
            print(f"Error returning My Account page heading: {e}")
            return None

    # ===== Logout Action =====

    def click_logout(self) -> LogoutPage:
        """Open My Account dropdown then click Logout link."""
        try:
            self.lnk_my_account.click()   # ← open dropdown first
            self.lnk_logout.click()       # ← then click Logout
            return LogoutPage(self.page)
        except Exception as e:
            print(f"Unable to click Logout link: {e}")
            raise e

    # ===== Page Title Verification =====

    def get_page_title(self) -> str:
        """Return the title of the current page."""
        try:
            return self.page.title()
        except Exception as e:
            print(f"Error retrieving page title: {e}")
            return ""


# # my_account_page.py
# from playwright.sync_api import Page
# from pages.logout_page import LogoutPage
#
#
# class MyAccountPage:
#     """Page Object Model class for the My Account Page."""
#
#     def __init__(self, page: Page):
#         self.page = page
#
#         # ===== Locators =====
#         self.msg_heading = page.locator('h1:has-text("My Account")')  # fixed h2 -> h1
#         self.lnk_logout = page.locator("text='Logout'").nth(1)
#
#     # ===== Page Validation Methods =====
#
#     def get_my_account_page_heading(self):
#         """Return the My Account page heading locator."""
#         try:
#             return self.msg_heading
#         except Exception as e:
#             print(f"Error returning My Account page heading: {e}")
#             return None
#
#     # ===== Logout Action =====
#
#     def click_logout(self) -> LogoutPage:
#         """Click the Logout link and return LogoutPage."""
#         try:
#             self.lnk_logout.click()
#             return LogoutPage(self.page)
#         except Exception as e:
#             print(f"Unable to click Logout link: {e}")
#             raise e
#
#     # ===== Page Title Verification =====
#
#     def get_page_title(self) -> str:
#         """Return the title of the current page."""
#         try:
#             return self.page.title()
#         except Exception as e:
#             print(f"Error retrieving page title: {e}")
#             return ""
#


# # my_account_page.py
# # =====================
# # This class represents the "My Account" page of the application.
# # It follows the Page Object Model (POM) pattern to separate
# # the page locators and actions from the actual test cases.
#
# from playwright.sync_api import Page, expect
# from pages.logout_page import LogoutPage  # Adjust import path based on your project structure
#
#
# class MyAccountPage:
#     """Page Object Model class for the My Account Page."""
#
#     def __init__(self, page: Page):
#         """
#         Constructor to initialize the Playwright Page instance
#         and define all locators present on the My Account page.
#         """
#         self.page = page
#
#         # ===== Locators =====
#         # Identifying elements on the My Account page.
#         self.msg_heading = page.locator('h2:has-text("My Account")')
#         self.lnk_logout = page.locator("text='Logout'").nth(1)
#
#     # ===== Page Validation Methods =====
#
#     def get_my_account_page_heading(self):
#         """
#         Returns the locator for the 'My Account' page heading.
#         Can be used in test assertions to verify page visibility.
#
#         Example:
#             expect(my_account_page.get_my_account_page_heading()).to_be_visible()
#         """
#         try:
#             return self.msg_heading
#         except Exception as e:
#             print(f"Error returning My Account page heading: {e}")
#             return None
#
#     # ===== Logout Action =====
#
#     def click_logout(self) -> LogoutPage:
#         """
#         Clicks on the 'Logout' link to log out the user.
#         Returns an instance of the LogoutPage class
#         to allow chained navigation in tests.
#
#         Example:
#             logout_page = my_account_page.click_logout()
#         """
#         try:
#             self.lnk_logout.click()
#             return LogoutPage(self.page)
#         except Exception as e:
#             print(f"Unable to click Logout link: {e}")
#             raise e  # Re-raise the exception to fail the test intentionally
#
#     # ===== Page Title Verification =====
#
#     def get_page_title(self) -> str:
#         """
#         Returns the title of the current page.
#
#         Example:
#             assert my_account_page.get_page_title() == "My Account"
#         """
#         try:
#             return self.page.title()
#         except Exception as e:
#             print(f"Error retrieving page title: {e}")
#             return ""
