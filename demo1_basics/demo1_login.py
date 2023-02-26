import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.facebook.com/')
#print title of the page
driver.maximize_window()
print(driver.title)
time.sleep(2)
driver.find_element(By.ID,"email").send_keys("testname@gmail.com")
driver.find_element(By.ID,"pass").send_keys("password")
driver.find_element(By.NAME,"login").click()
time.sleep(2)