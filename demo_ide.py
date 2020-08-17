import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

## Create By Selenium IDE
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # Web Driver Set
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_untitled(self):
        # Open
        self.driver.get("https://www.hatena.ne.jp/")
        # Text Input
        self.driver.find_element_by_name("q").send_keys("はてな")
        # Click
        self.driver.find_element_by_css_selector(".gsc-search-button").click()
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()