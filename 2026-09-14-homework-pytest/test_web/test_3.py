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


def test_contact_7(driver):
    driver.find_element(By.LINK_TEXT, "Contact Us").click()
    driver.find_element(By.ID, "full-name").send_keys("Eldar Bakshi")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "submit-btn").click()
    status_message_element = driver.find_element(By.ID, "status-message")
    assert status_message_element.text == "Error: You must accept the terms!"
    assert status_message_element.value_of_css_property("color") == "rgba(255, 0, 0, 1)"

def test_contact_8(driver):
    driver.find_element(By.LINK_TEXT, "Contact Us").click()
    driver.find_element(By.ID, "full-name").send_keys("Eldar Bakshi")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "terms-check").click()
    driver.find_element(By.ID, "submit-btn").click()

    status_message_element = driver.find_element(By.ID, "status-message")
    assert status_message_element.text == "Success: Thank you Eldar Bakshi, registration complete!"
    assert status_message_element.value_of_css_property("color") == "rgba(0, 128, 0, 1)"
