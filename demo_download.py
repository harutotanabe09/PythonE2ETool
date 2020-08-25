import unittest
import os
import time
import csv

from pathlib import Path  # 絶対パスを簡単に取得できるように
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

## Create By Selenium IDE
class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        # Download Path
        dldir_name = 'download1'
        dldir_path = Path(dldir_name)
        dldir_path.mkdir(exist_ok=True)
        download_dir = str(dldir_path.resolve())
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
            "plugins.always_open_pdf_externally": True
        })
        # Web Driver Set
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)

    def test_execute(self):
        driver = self.driver
        # Open
        driver.get("https://pythonchannel.com/media/codecamp/201908-/scrape-test.html")
        # Download
        download_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/a")))
        download_button.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()