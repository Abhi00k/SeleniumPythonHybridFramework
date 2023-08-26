from pages.HomePage import HomePage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils


class TestRegister(BaseTest):
    # reading data from excel files
    def test_register_with_mandatory_field(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account(
            ExcelUtils.get_cell_data("ExcelFiles/TutorialsNinja.xlsx", "RegisterTest", 2, 1),
            ExcelUtils.get_cell_data("ExcelFiles/TutorialsNinja.xlsx", "RegisterTest", 2, 2),
            self.generate_email_with_time_stamp(), "12345667898", "1234567", "1234567", "no", "select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account("Abhishek", "Kumar",
                                                                 self.generate_email_with_time_stamp(), "12345667898",
                                                                 "1234567", "1234567", "no", "select")
        expected_heading_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_heading_text)

    def test_register_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("Abhishek", "Kumar", "kumar.abhishek150792@gmail.com", "12345667898",
                                          "1234567", "1234567", "no", "select")
        expected_warning_message = "Warning: E-Mail Address is already registered!ABC"
        assert register_page.retrieve_duplicate_email_warning().__contains__(expected_warning_message)

    def test_register_without_entry_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account("", "", "", "",
                                          "", "", "no", "no")
        assert register_page.verify_all_warnings("Warning: You must agree to the Privacy Policy!",
                                                 "First Name must be between 1 and 32 characters!",
                                                 "Last Name must be between 1 and 32 characters!",
                                                 "E-Mail Address does not appear to be valid!",
                                                 "Telephone must be between 3 and 32 characters!",
                                                 "Password must be between 4 and 20 characters!")
