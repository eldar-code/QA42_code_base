from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/tables.html")
driver.maximize_window()

# Tar1 - find the table
table = driver.find_element(By.TAG_NAME, "table")
# find all header names and put in a list
header_names = []
for th in table.find_elements(By.TAG_NAME, "th"):
    header_names.append(th.text)

# print all the found header names
print(header_names)
print("===================")
# Tar2
ids: list[int] = []
names: list[str] = []
ages: list[int] = []

tbody = table.find_element(By.TAG_NAME, "tbody")

for tr in tbody.find_elements(By.TAG_NAME, "tr"):
    tds = tr.find_elements(By.TAG_NAME, "td")
    ids.append(int(tds[0].text))
    names.append(tds[1].text)
    ages.append(int(tds[2].text))

print(ids)
print(names)
print(ages)


driver.close()
