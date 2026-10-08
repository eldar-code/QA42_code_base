from time import sleep
from unittest import TestCase
from selenium import webdriver


# TestDom is a class. From a class we create objects.
# The parameter "self" is a reference to the current TestDom object.
# To create data that is available on each method we append it to self.
class TestDom(TestCase):

    # initial actions before each test
    def setUp(self):
        # self is a reference to the current TestDom object
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:5500/index.html")
        self.driver.maximize_window()

    # final actions after each test
    def tearDown(self):
        sleep(3)
        self.driver.close()

    def test_page_title(self):
        page_title = self.driver.title
        self.assertEqual("DOM", page_title)
