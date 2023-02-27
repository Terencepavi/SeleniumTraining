import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://netbanking.hdfcbank.com/netbanking/')
driver.implicitly_wait(10)
#print title of the page
driver.maximize_window()
print(driver.title)
driver.switch_to.frame(driver.find_element(By.XPATH,"//frame[@name='login_page']"))
driver.find_element(By.XPATH,("//input[@name='fldLoginUserId']")).send_keys("test123")
driver.find_element(By.XPATH,("//a[normalize-space()='CONTINUE']")).click()
#Switch to main frame or parent frame
driver.switch_to.default_content()