from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")
driver.maximize_window()

# find the elements in the DOM
div = driver.find_element(By.ID, "x")
inp = driver.find_element(By.ID, "y")

# to get access to the div text use "innerHTML"
print(div.text)
# to get access to the input text use "value"
print(inp.get_attribute("value"))
sleep(5)

# click the button
driver.find_element(By.TAG_NAME, "button").click()
sleep(5)

# to get access to the div text use "innerHTML"
print(div.text)
# to get access to the input text use "value"
print(inp.get_attribute("value"))
sleep(5)

driver.close()