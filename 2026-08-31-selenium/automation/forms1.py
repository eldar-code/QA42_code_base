from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://127.0.0.1:5500/")

# fill the first name input
sleep(3)
driver.find_element(By.ID, "in_first").send_keys("Dan")
# fill the last name input
sleep(1)
driver.find_element(By.ID, "in_last").send_keys("Braun")
# fill the email input
sleep(1)
driver.find_element(By.ID, "in_email").send_keys("dan@mail")
# click submit
sleep(1)
driver.find_element(By.ID, "in_submit_1").click()
# click the link to go back to Home Page
sleep(3)
driver.find_element(By.LINK_TEXT, "Home Page").click()

sleep(5)
driver.close()