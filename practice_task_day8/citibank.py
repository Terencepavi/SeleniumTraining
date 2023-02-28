import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

driver = webdriver.Chrome()
driver.get('https://www.online.citibank.co.in/')
#print title of the page
driver.implicitly_wait(10)
driver.maximize_window()
driver.find_element(By.XPATH,("//a[@title='Close']")).click()
driver.find_element(By.XPATH,("//span[@class='txtSign']")).click()
parentwindow=driver.current_window_handle
print("parent window id is:",parentwindow)
windows=driver.window_handles
print("All Windows\n:",windows)
driver.switch_to.window(windows[1])
driver.find_element(By.XPATH,("//div[contains(text(),' Forgot User ID? ')]")).click()
driver.find_element(By.XPATH,('//a[@class="sbSelector"]')).click()
driver.find_element(By.XPATH,("//a[contains(text(),'Credit Card')]")).click()
driver.find_element(By.XPATH,('//input[@class="numberField debit-num"]')).send_keys("4545565688879998")
driver.find_element(By.XPATH,("//input[@id='cvvnumber']")).send_keys("123")
driver.find_element(By.XPATH,("//input[@id='bill-date-long']")).click()
year=Select(driver.find_element(By.XPATH,('//select[@data-handler="selectYear"]')))
year.select_by_visible_text("2022")
month=Select(driver.find_element(By.XPATH,('//select[@data-handler="selectMonth"]')))
month.select_by_visible_text("Apr")
driver.find_element(By.XPATH,("//a[contains(text(),'14')]")).click()
time.sleep(2)
# driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH('//input[@value="PROCEED"]'
# footer=driver.find_element(By.XPATH("div[class='footerLogo']"))
# driver.execute_script("arguments[0].scrollintoView();",footer)
driver.execute_script("window.scrollBy(0,1000)","")
time.sleep(5)
driver.find_element(By.XPATH,("//div[3]/div[12]/div[1]/input[1]")).click()
# time.sleep(2)
# driver.switch_to.alert.accept()
wait=WebDriverWait(driver,20)
errortab=wait.until(Ec.presence_of_element_located((By.XPATH,("//li[contains(text(),'• Please accept Terms and Conditions')]"))))
errormsg=errortab.text
print("Error message:",errormsg)

# print(errormsg)