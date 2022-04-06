from datetime import time

from selenium import webdriver
   #from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
   #from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:\Webdriver\chromedriver.exe")
driver.get("https://divyanshi13-trials7401.orangehrmlive.com/")
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.maximize_window()
driver.find_element(By.ID, "txtPassword").send_keys("ReRL4@hMw7")
button = driver.find_element(By.CLASS_NAME, "button-holder")
button.click()

# driver = webdriver.Chrome("C:\Program Files\Webdrivers\chromedriver.exe")
def alert_pop():
    driver.get("https://divyanshi13-trials7401.orangehrmlive.com/")

button = driver.find_element(By.ID, "account-name")
button.click()
button = driver.find_element(By.ID, "aboutDisplayLink")
button.click()
time.sleep(5)