from playwright.sync_api import Page

class HomePage:
    """Page Object Model class for the 'Home' page."""

    def __init__(self, page: Page):
        self.page = page

        # ===== Locators =====
        self.lnk_my_account = self.page.locator('span:has-text("My Account")')
        self.lnk_register   = self.page.locator('a:has-text("Register")')
        self.lnk_login      = self.page.locator('a:has-text("Login")')
        self.txt_search_box = self.page.locator('input[name="search"]')
        self.btn_search     = self.page.locator('button[type="submit"].btn-light')  # ← fixed

    # ===== Action Methods =====

    def get_home_page_title(self) -> str:
        """Return the title of the Home Page."""
        return self.page.title()

    def click_my_account(self):
        """Click on the 'My Account' link."""
        try:
            self.lnk_my_account.click()
        except Exception as e:
            print(f" Exception while clicking 'My Account': {e}")
            raise

    def click_register(self):
        """Click on the 'Register' link under My Account."""
        try:
            self.lnk_register.click()
            self.page.wait_for_load_state("networkidle")
        except Exception as e:
            print(f" Exception while clicking 'Register': {e}")
            raise

    def click_login(self):
        """Click on the 'Login' link under My Account."""
        try:
            self.lnk_login.click()
            self.page.wait_for_load_state("networkidle")
        except Exception as e:
            print(f" Exception while clicking 'Login': {e}")
            raise

    def enter_product_name(self, product_name: str):
        """Enter the product name into the search input box."""
        try:
            self.txt_search_box.fill(product_name)
        except Exception as e:
            print(f" Exception while entering product name '{product_name}': {e}")
            raise

    def click_search(self):
        """Click on the search button to initiate the product search."""
        try:
            self.btn_search.click()
        except Exception as e:
            print(f" Exception while clicking 'Search' button: {e}")
            raise

    def enter_search_text(self, text: str):
        """Alias for enter_product_name — used in search tests."""
        self.txt_search_box.fill(text)

    def click_search_button(self):
        """Alias for click_search — used in search tests."""
        self.btn_search.click()

# from playwright.sync_api import Page
#
# class HomePage:
#     """Page Object Model class for the 'Home' page."""
#
#     def __init__(self, page: Page):
#         """
#         Constructor to initialize the Playwright page object
#         and define all necessary locators.
#         """
#         self.page = page
#
#         # ===== Locators =====
#         self.lnk_my_account = self.page.locator('span:has-text("My Account")')
#         self.lnk_register = self.page.locator('a:has-text("Register")')
#         self.lnk_login = self.page.locator('a:has-text("Login")')
#         self.txt_search_box = self.page.locator('input[placeholder="Search"]')
#         self.btn_search = self.page.locator('#search button[type="button"]')
#
#     # ===== Action Methods =====
#
#     def get_home_page_title(self) -> str:
#         """Return the title of the Home Page."""
#         return self.page.title()
#
#     def click_my_account(self):
#         """Click on the 'My Account' link."""
#         try:
#             self.lnk_my_account.click()
#         except Exception as e:
#             print(f" Exception while clicking 'My Account': {e}")
#             raise
#
#     def click_register(self):
#         """Click on the 'Register' link under My Account."""
#         try:
#             self.lnk_register.click()
#             self.page.wait_for_load_state("networkidle")  # wait for registration page to fully load
#         except Exception as e:
#             print(f" Exception while clicking 'Register': {e}")
#             raise
#
#     def click_login(self):
#         """Click on the 'Login' link under My Account."""
#         try:
#             self.lnk_login.click()
#             self.page.wait_for_load_state("networkidle")  # wait for login page to fully load
#         except Exception as e:
#             print(f" Exception while clicking 'Login': {e}")
#             raise
#
#     def enter_product_name(self, product_name: str):
#         """Enter the product name into the search input box."""
#         try:
#             self.txt_search_box.fill(product_name)
#         except Exception as e:
#             print(f" Exception while entering product name '{product_name}': {e}")
#             raise
#
#     def click_search(self):
#         """Click on the search button to initiate the product search."""
#         try:
#             self.btn_search.click()
#         except Exception as e:
#             print(f" Exception while clicking 'Search' button: {e}")
#             raise
#
#     def enter_search_text(self, text: str):
#         self.page.locator("input[name='search']").fill(text)
#
#     def click_search_button(self):
#         self.page.locator("button[type='submit'].btn-light").click()


# from playwright.sync_api import Page
#
# class HomePage:
#     """Page Object Model class for the 'Home' page."""
#
#     def __init__(self, page: Page):
#         """
#         Constructor to initialize the Playwright page object
#         and define all necessary locators.
#         """
#         self.page = page
#
#         # ===== Locators =====
#         # Using Playwright's 'locator' method to identify UI elements
#         self.lnk_my_account = self.page.locator('span:has-text("My Account")')
#         self.lnk_register = self.page.locator('a:has-text("Register")')
#         self.lnk_login = self.page.locator('a:has-text("Login")')
#         self.txt_search_box = self.page.locator('input[placeholder="Search"]')
#         self.btn_search = self.page.locator('#search button[type="button"]')
#
#     # ===== Action Methods =====
#     # Each method represents a user interaction on the page
#
#     def get_home_page_title(self) -> str:
#         """Return the title of the Home Page."""
#         title = self.page.title()
#         return title
#
#     def click_my_account(self):
#         """Click on the 'My Account' link."""
#         try:
#             self.lnk_my_account.click()
#         except Exception as e:
#             print(f" Exception while clicking 'My Account': {e}")
#             raise
#
#     def click_register(self):
#         """Click on the 'Register' link under My Account."""
#         try:
#             self.lnk_register.click()
#         except Exception as e:
#             print(f" Exception while clicking 'Register': {e}")
#             raise
#
#     def click_login(self):
#         """Click on the 'Login' link under My Account."""
#         try:
#             self.lnk_login.click()
#         except Exception as e:
#             print(f" Exception while clicking 'Login': {e}")
#             raise
#
#     def enter_product_name(self, product_name: str):
#         """Enter the product name into the search input box."""
#         try:
#             self.txt_search_box.fill(product_name)
#         except Exception as e:
#             print(f" Exception while entering product name '{product_name}': {e}")
#             raise
#
#     def click_search(self):
#         """Click on the search button to initiate the product search."""
#         try:
#             self.btn_search.click()
#         except Exception as e:
#             print(f" Exception while clicking 'Search' button: {e}")
#             raise
