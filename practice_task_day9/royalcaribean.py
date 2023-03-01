import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

driver = webdriver.Chrome()
driver.get('https://www.royalcaribbean.com')
driver.maximize_window()
driver.find_element(By.XPATH,'(//span[text()="Sign In"])[1]').click()
wait=WebDriverWait(driver,20)
action=webdriver.ActionChains(driver)
time.sleep(10)
# action.scroll_to_element(driver.find_element(By.XPATH,'//a[text()="Create an account"]'))
driver.find_element(By.LINK_TEXT,'Create an account').click()
