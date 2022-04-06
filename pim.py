from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("C:\Webdriver\chromedriver.exe")
driver.get("https://divyanshi13-trials7401.orangehrmlive.com/")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
time.sleep(3)
driver.find_element_by_id("txtPassword").send_keys("ReRL4@hMw7")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="divLogin"]/div[2]/div/form/div[3]/button').click()
time.sleep(3)
driver.find_element(By.ID,"menu_pim_viewPimModule").click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="menu_pim_addEmployee"]/span[2]').click()
time.sleep(3)

# ente first name
driver.find_element(By.CSS_SELECTOR,"#first-name-box").send_keys("himanshu")
# enter middle name
driver.find_element(By.CSS_SELECTOR,"#middle-name-box").send_keys("kumar")
# enter last name
driver.find_element(By.XPATH,'//*[@id="last-name-box"]').send_keys("rajput")
# enter employee id
driver.find_element(By.ID,"employeeId").send_keys(9470)

driver.find_element(By.CSS_SELECTOR,"#modal-holder > div > div > div > div.modal-body > form > oxd-decorator > div > div.form-group.col-8 > div > div:nth-child(2) > div > div.form-group.col-5.remove-right-padding > div > div.dropdown.bootstrap-select.select-dropdown > button").click()
time.sleep(3)
#location
driver.find_element(By.XPATH,"//*[@id='bs-select-1-7']").click()
#next button
driver.find_element(By.XPATH,'//*[@id="modal-save-button"]').click()