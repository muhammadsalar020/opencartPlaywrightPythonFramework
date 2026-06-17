# logout_page.py
from playwright.sync_api import Page


class LogoutPage:
    """Page Object Model class for the Logout Page."""

    def __init__(self, page: Page):
        self.page = page

        # ===== Locators =====
        self.btn_continue     = page.locator('.btn.btn-primary')
        self.heading_logout   = page.locator('#content h1')  # "Account Logout"

    # ===== Action Methods =====

    def click_continue(self):
        """Click the Continue button after logging out."""
        try:
            self.btn_continue.click()
        except Exception as e:
            print(f" Exception while clicking 'Continue' button: {e}")
            raise

    def get_continue_button(self):
        """Return the Continue button locator."""
        try:
            return self.btn_continue
        except Exception as e:
            print(f" Exception while fetching 'Continue' button locator: {e}")
            return None

    def get_logout_page_heading(self):
        """Return the 'Account Logout' heading locator."""
        return self.heading_logout