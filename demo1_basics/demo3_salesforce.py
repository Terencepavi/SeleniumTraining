import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")

driver.find_element(By.NAME, 'UserFirstName').send_keys('John')
driver.find_element(By.NAME, 'UserLastName').send_keys('wick')
driver.find_element(By.NAME, 'UserEmail').send_keys('john@gmail.com')
driver.find_element(By.NAME, 'CompanyName').send_keys('eInfochip')
Select(driver.find_element(By.NAME, 'UserTitle')).select_by_value('Developer')
Select(driver.find_element(By.NAME, 'CompanyEmployees')).select_by_value('950')
Select(driver.find_element(By.NAME, 'CompanyCountry')).select_by_visible_text('Germany')
driver.find_element(By.NAME, 'start my free trial').click()
error_message = driver.find_element(By.XPATH,"//span[contains(@id,'UserPhone-')]").text
assert error_message == 'Enter a valid phone number'

time.sleep(10)



