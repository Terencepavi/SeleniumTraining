import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.medibuddy.in')
#print title of the page
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.XPATH,("//a[contains(text(),'Login')]")).click()
driver.find_element(By.XPATH,("//div[contains(text(),'I have a Corporate Account')]")).click()
driver.find_element(By.XPATH,("//div[contains(text(),'Login using Username & Password')]")).click()
driver.find_element(By.NAME,"userName").send_keys("John")
driver.find_element(By.XPATH,("//button[contains(text(),'Proceed')]")).click()
driver.find_element(By.NAME,"password").send_keys("john123")
driver.find_element(By.XPATH,("//label[@class='showpass']")).click()
driver.find_element(By.XPATH,("//button[contains(text(),'Log in')]")).click()
errormsg=driver.find_element(By.XPATH,("//div[contains(text(),'You have entered incorrect password. If you forgot')]")).text
print(errormsg)

time.sleep(5)