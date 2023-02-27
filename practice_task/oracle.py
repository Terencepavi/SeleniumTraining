import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.oracle.com/in/database')
#print title of the page
driver.implicitly_wait(10)
driver.maximize_window()
print(driver.title)
driver.find_element(By.ID,"acctBtnLabel").click()
driver.find_element(By.LINK_TEXT,"Sign-In").click()
# pageheader=driver.find_element(By.XPATH,("//h2[contains(text(),'Oracle account sign in')]")).text
# print(pageheader)
driver.find_element(By.ID,'sso_username').send_keys('John')
driver.find_element(By.ID,'ssopassword').send_keys('Test@123')
driver.find_element(By.XPATH,("//input[@id='signin_button']")).click()
errormsg=driver.find_element(By.XPATH,("//div[contains(text(),'Invalid username and/or password.')]")).text
assert errormsg == 'Invalid username and/or password.'