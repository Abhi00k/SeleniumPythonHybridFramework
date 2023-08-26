from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class TestSearch(BaseTest):
    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("HP")
        assert search_page.display_status_of_valid_product()

    def test_search_for_a_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("Honda")
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrieve_no_product_message().__eq__(expected_text)

    def test_search_without_entry_any_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product("")
        expected_text = "There is no product that matches the search criteria."
        assert search_page.retrieve_no_product_message().__eq__(expected_text)
