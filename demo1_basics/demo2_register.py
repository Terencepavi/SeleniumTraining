import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
#print title of the page
driver.maximize_window()
driver.implicitly_wait(10)
print(driver.title)
driver.find_element(By.LINK_TEXT,"Create new account").click()
print("signup url is:\n",driver.current_url)
# time.sleep(2) # No such element error giving due to non-sync without sleep
driver.find_element(By.NAME,"firstname").send_keys("Joseph")
driver.find_element(By.NAME,"lastname").send_keys("kuiruvila")
driver.find_element(By.NAME,"reg_passwd__").send_keys("welcome123")
driver.find_element(By.XPATH,'(//input[@type="radio"])[2]').click()

birth_date = Select ( driver.find_element(By.ID,"day"))
birth_date.select_by_visible_text("17")

birth_month = Select ( driver.find_element(By.ID,"month"))
birth_month.select_by_visible_text("May")

birth_year = Select ( driver.find_element(By.ID,"year"))
birth_year.select_by_visible_text("1997")
