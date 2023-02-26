import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.db4free.net/')
driver.implicitly_wait(10)
#print title of the page
driver.maximize_window()
print(driver.title)
driver.find_element(By.PARTIAL_LINK_TEXT, "phpMyAdmi").click()

Windows=driver.window_handles
print(Windows)
driver.switch_to.window(Windows[1])
driver.find_element(By.ID,"input_username").send_keys("CaptainJacksparrow")
driver.find_element(By.ID,"input_password").send_keys("welcome@123")
driver.find_element(By.ID,"input_go").click()
driver.switch_to.window(Windows[0])

time.sleep(10)
