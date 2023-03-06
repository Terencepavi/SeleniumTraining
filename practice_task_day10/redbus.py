import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.redbus.in/")

driver.find_element(By.XPATH,"//i[@id='i-icon-profile']").click()
driver.find_element(By.XPATH,"//div[@id='hc']").click()
driver.switch_to.frame(driver.find_element(By.XPATH,"//div[@class='modal']//iframe[@class='modalIframe']"))
driver.find_element(By.XPATH,"//input[@id='mobileNoInp']").send_keys(9787)
error_msg = driver.find_element(By.XPATH,"//span[@class='error-message-fixed error-message-full top-fix']").text
print(error_msg)
driver.quit()