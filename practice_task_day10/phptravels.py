import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.phptravels.net/")
driver.find_element(By.XPATH,"//button[@id='languages']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='English']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='flights']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='autocomplete']").send_keys("MAA - Chennai Intl - Madras")
driver.find_element(By.XPATH,"//input[@id='autocomplete2']").send_keys("LGA - La Guardia - New York")
time.sleep(2)
driver.find_element(By.XPATH,"//div[@class='row g-0']//input[@id='departure']").clear()
driver.find_element(By.XPATH,"(//input[@id='departure'])[1]").send_keys("2023-04-14")
time.sleep(2)
driver.find_element(By.XPATH,"//a[@role='button']").click()
driver.find_element(By.XPATH,"//div[@class='dropdown-item adult_qty']//i[@class='la la-plus']").click()
driver.find_element(By.XPATH,"//span[@class='ladda-label']//*[name()='svg']").click()
time.sleep(2)
result=driver.find_element(By.XPATH,"//li[1]//div[1]//form[1]").text
print("First flight details:\n",result)
driver.quit()