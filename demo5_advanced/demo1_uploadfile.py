import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.ilovepdf.com/pdf_to_word')
driver.implicitly_wait(10)
#print title of the page
driver.maximize_window()
print(driver.title)
driver.find_element(By.XPATH,"//input[@type='file']").send_keys(r"C:\Users\153500\Downloads\Invoice_jan2023.pdf")
time.sleep(5)