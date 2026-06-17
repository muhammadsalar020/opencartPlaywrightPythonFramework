# registration_page.py
from playwright.sync_api import Page


class RegistrationPage:
    """
    Page Object Model class for the Registration Page.
    """

    def __init__(self, page: Page):
        self.page = page

        # ===== Locators =====
        self.txt_firstname    = page.locator('#input-firstname')
        self.txt_lastname     = page.locator('#input-lastname')
        self.txt_email        = page.locator('#input-email')
        self.txt_password     = page.locator('#input-password')
        self.chk_policy       = page.locator('input[name="agree"]')
        self.btn_continue     = page.locator('button.btn-primary:has-text("Continue")')
        self.msg_confirmation = page.locator('h1:has-text("Your Account Has Been Created!")')

    # ===== Action Methods =====

    def set_first_name(self, fname: str):
        """Enter the user's first name."""
        self.txt_firstname.fill(fname)

    def set_last_name(self, lname: str):
        """Enter the user's last name."""
        self.txt_lastname.fill(lname)

    def set_email(self, email: str):
        """Enter the user's email address."""
        self.txt_email.fill(email)

    def set_password(self, pwd: str):
        """Enter the password."""
        self.txt_password.fill(pwd)

    def set_privacy_policy(self):
        """Click the Privacy Policy checkbox to agree."""
        self.chk_policy.click()

    def click_continue(self):
        """Click the Continue button and wait for page to load."""
        self.btn_continue.click()
        self.page.wait_for_load_state("networkidle")  # ← fixed (removed expect_navigation)

    def get_confirmation_msg(self):
        """Return the confirmation message locator."""
        return self.msg_confirmation

    # ===== Combined Workflow =====

    def complete_registration(self, user_data: dict):
        """
        Complete the full registration process using provided user data.

        Example:
        user_data = {
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "password": "Test@123"
        }
        """
        self.set_first_name(user_data["firstName"])
        self.set_last_name(user_data["lastName"])
        self.set_email(user_data["email"])
        self.set_password(user_data["password"])
        self.set_privacy_policy()
        self.click_continue()
        return self.msg_confirmation



# # registration_page.py
# from playwright.sync_api import Page
#
#
# class RegistrationPage:
#     """
#     Page Object Model class for the Registration Page.
#     """
#
#     def __init__(self, page: Page):
#         self.page = page
#
#         # ===== Locators =====
#         self.txt_firstname = page.locator('#input-firstname')
#         self.txt_lastname = page.locator('#input-lastname')
#         self.txt_email = page.locator('#input-email')
#         self.txt_password = page.locator('#input-password')
#
#         # Privacy Policy toggle and Continue button
#         self.chk_policy = page.locator('input[name="agree"]')
#         self.btn_continue = page.locator('button.btn-primary:has-text("Continue")')
#
#         # Confirmation — success page shown after registration
#         self.msg_confirmation = page.locator('h1:has-text("Your Account Has Been Created!")')
#
#     # ===== Action Methods =====
#
#     def set_first_name(self, fname: str):
#         """Enter the user's first name."""
#         self.txt_firstname.fill(fname)
#
#     def set_last_name(self, lname: str):
#         """Enter the user's last name."""
#         self.txt_lastname.fill(lname)
#
#     def set_email(self, email: str):
#         """Enter the user's email address."""
#         self.txt_email.fill(email)
#
#     def set_password(self, pwd: str):
#         """Enter the password."""
#         self.txt_password.fill(pwd)
#
#     def set_privacy_policy(self):
#         """Click the Privacy Policy toggle to agree."""
#         self.chk_policy.click()
#
#     def click_continue(self):
#         """Click the Continue button and wait for navigation."""
#         with self.page.expect_navigation():
#             self.btn_continue.click()
#
#     def get_confirmation_msg(self):
#         """Return the confirmation message locator."""
#         return self.msg_confirmation
#
#     # ===== Combined Workflow =====
#
#     def complete_registration(self, user_data: dict):
#         """
#         Complete the full registration process using provided user data.
#
#         Example:
#         user_data = {
#             "firstName": "John",
#             "lastName": "Doe",
#             "email": "john.doe@example.com",
#             "password": "Test@123"
#         }
#         """
#         self.set_first_name(user_data["firstName"])
#         self.set_last_name(user_data["lastName"])
#         self.set_email(user_data["email"])
#         self.set_password(user_data["password"])
#         self.set_privacy_policy()
#         self.click_continue()
#
#         return self.msg_confirmation
#

# # registration_page.py
# from playwright.sync_api import Page
#
#
# class RegistrationPage:
#     """
#     Page Object Model class for the Registration Page.
#     This class contains web element locators and methods (actions)
#     to interact with the registration form.
#     """
#
#     def __init__(self, page: Page):
#         self.page = page
#
#         # ===== Locators =====
#         # Input fields
#         self.txt_firstname = page.locator('#input-firstname')
#         self.txt_lastname = page.locator('#input-lastname')
#         self.txt_email = page.locator('#input-email')
#         self.txt_telephone = page.locator('#input-telephone')
#         self.txt_password = page.locator('#input-password')
#         self.txt_confirm_password = page.locator('#input-confirm')
#
#         # Checkbox and buttons
#         self.chk_policy = page.locator('input[name="agree"]')
#         self.btn_continue = page.locator('input[value="Continue"]')
#
#         # Confirmation message (displayed after successful registration)
#         self.msg_confirmation = page.locator('h1:has-text("Your Account Has Been Created!")')
#
#     # ===== Action Methods =====
#
#     def set_first_name(self, fname: str):
#         """Enter the user's first name into the 'First Name' field."""
#         self.txt_firstname.fill(fname)
#
#     def set_last_name(self, lname: str):
#         """Enter the user's last name into the 'Last Name' field."""
#         self.txt_lastname.fill(lname)
#
#     def set_email(self, email: str):
#         """Enter the user's email address."""
#         self.txt_email.fill(email)
#
#     def set_telephone(self, tel: str):
#         """Enter the user's telephone number."""
#         self.txt_telephone.fill(tel)
#
#     def set_password(self, pwd: str):
#         """Enter the password."""
#         self.txt_password.fill(pwd)
#
#     def set_confirm_password(self, pwd: str):
#         """Re-enter the password in the 'Confirm Password' field."""
#         self.txt_confirm_password.fill(pwd)
#
#     def set_privacy_policy(self):
#         """Select the 'Privacy Policy' checkbox."""
#         self.chk_policy.check()
#
#     def click_continue(self):
#         """Click on the 'Continue' button to submit the registration form."""
#         self.btn_continue.click()
#
#     def get_confirmation_msg(self):
#         """
#         Return the confirmation message locator.
#         This can be used to verify successful registration.
#         """
#         return self.msg_confirmation
#
#     # ===== Combined Workflow =====
#
#     def complete_registration(self, user_data: dict):
#         """
#         Complete the full registration process using provided user data.
#
#         Example:
#         user_data = {
#             "firstName": "John",
#             "lastName": "Doe",
#             "email": "john.doe@example.com",
#             "telephone": "9876543210",
#             "password": "Test@123"
#         }
#         """
#         self.set_first_name(user_data["firstName"])
#         self.set_last_name(user_data["lastName"])
#         self.set_email(user_data["email"])
#         self.set_telephone(user_data["telephone"])
#         self.set_password(user_data["password"])
#         self.set_confirm_password(user_data["password"])
#         self.set_privacy_policy()
#         self.click_continue()
#
#         # Return confirmation message element for validation
#         return self.msg_confirmation
