import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://nasscom.in/')
# print title of the page
driver.implicitly_wait(10)
driver.maximize_window()

action = webdriver.ActionChains(driver)
action.move_to_element(driver.find_element(By.LINK_TEXT, "Membership")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Become a Member")).perform()
driver.find_element(By.LINK_TEXT, "Membership Benefits").click()
time.sleep(5)
driver.quit()
