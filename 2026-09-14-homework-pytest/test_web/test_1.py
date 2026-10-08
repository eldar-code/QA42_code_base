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


def test_home_1(driver):
    assert driver.title == "QA Practice - Home"
    h1_list = driver.find_elements(By.TAG_NAME, "h1")
    assert len(h1_list) == 1
    assert h1_list[0].text == "Welcome to QA Testing Portal"


def test_home_2(driver):
    list_p = driver.find_element(By.CLASS_NAME, "content-box").find_elements(By.CLASS_NAME, "article-text")
    assert len(list_p) == 12
    for p in list_p:
        assert p.text.startswith("Paragraph")


def test_home_3(driver):
    show_bt = driver.find_element(By.ID, "toggle-btn")
    show_bt.click()
    assert show_bt.text == "Hide Message"
    secret_message = driver.find_element(By.ID, "secret-message")
    assert secret_message.text == "Hidden Automation Message Revealed!"
    show_bt.click()
    assert show_bt.text == "Show Message"
    assert not secret_message.is_displayed()


def test_home_4(driver):
    # insert text into input field
    driver.find_element(By.ID, "user-input").send_keys("Selenium Test Passed")
    # click the update button
    driver.find_element(By.ID, "update-btn").click()
    # check that the dynamic heading has changed
    assert driver.find_element(By.ID, "dynamic-heading").text == "Selenium Test Passed"
