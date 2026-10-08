import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def driver():
    driver = Chrome()
    driver.get("http://127.0.0.1:5500/")
    driver.maximize_window()
    yield driver
    time.sleep(1)
    driver.quit()


def test_table_5(driver):
    driver.find_element(By.LINK_TEXT, "Data Tables").click()
    header_rows_list = driver.find_element(By.TAG_NAME, "thead").find_elements(By.TAG_NAME, "tr")
    assert len(header_rows_list) == 1
    header_col_list = header_rows_list[0].find_elements(By.TAG_NAME, "th")
    assert len(header_col_list) == 4
    tbody = driver.find_element(By.TAG_NAME, "tbody")
    tbody_row_list = tbody.find_elements(By.TAG_NAME, "tr")
    assert len(tbody_row_list) == 15
    assert driver.find_element(By.ID, "row-counter").text == "Total Rows: 15"

def test_table_6(driver):
    driver.find_element(By.LINK_TEXT, "Data Tables").click()
    table_search_input = driver.find_element(By.ID, "table-search")
    table_search_input.send_keys("QA")
    tbody = driver.find_element(By.TAG_NAME, "tbody")
    tbody_row_list = tbody.find_elements(By.TAG_NAME, "tr")
    counter = 0
    for row in tbody_row_list:
        if row.is_displayed():
            counter += 1
    assert counter == 4
    assert driver.find_element(By.ID, "row-counter").text == "Total Rows: 4"


