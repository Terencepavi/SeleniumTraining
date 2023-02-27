import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://netbanking.hdfcbank.com/netbanking/IpinResetUsingOTP.htm')
# To inspect à ctrl+shift+c or f12
driver.implicitly_wait(10)
#print title of the page
driver.maximize_window()
print(driver.title)
driver.find_element(By.XPATH,"//img[@alt='Go']").click()
actual_alert_text=driver.switch_to.alert.text
print(actual_alert_text)
driver.switch_to.alert.accept()
