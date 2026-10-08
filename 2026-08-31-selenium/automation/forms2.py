from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://127.0.0.1:5500/")

# find the select element in form 2
sel_element = driver.find_element(By.ID, "in_country")
# create a Select object from the select element
sel_object = Select(sel_element)

# there are 3 ways to select an option from a select object:
# 1. by index
sleep(3)
sel_object.select_by_index(4)
# 2. by value (recommended)
sleep(3)
sel_object.select_by_value("il")
# 3. by visible text
sleep(3)
sel_object.select_by_visible_text("USA")

# send the form
sleep(3)
driver.find_element(By.ID, "in_submit_2").click()
# wait 5 seconds in Sever Page
sleep(5)
# go back - by navigating back
driver.back()

sleep(5)
driver.close()