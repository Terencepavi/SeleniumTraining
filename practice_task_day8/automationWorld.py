import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

driver = webdriver.Chrome()
driver.get('https://www.automationworld.com/')
driver.implicitly_wait(10)
#print title of the page
driver.maximize_window()
wait=WebDriverWait(driver,20)
popup=wait.until(Ec.presence_of_element_located((By.XPATH,('//div[@class="close-olytics-image-bottom-middarkblue"]'))))
popup.click()
driver.find_element(By.XPATH,('(//span[text()="Subscribe"])[1]')).click()
windows=driver.window_handles
driver.switch_to.window(windows[1])
driver.find_element(By.XPATH,"//input[@id='id24_344']").click()
driver.find_element(By.XPATH,"//input[@id='id1']").send_keys("Testusername")
driver.find_element(By.XPATH,"//input[@id='id2']").send_keys("Tes@123")
driver.find_element(By.XPATH,"//input[@id='id10']").send_keys("Tester")
# driver.find_element(By.XPATH,"//input[@id='id13']").send_keys("test@email.com")
driver.find_element(By.XPATH,"//input[@id='id195']").send_keys("www.test.com")
driver.find_element(By.XPATH,"//input[@id='id11']").send_keys("1234567890")
country=Select(driver.find_element(By.XPATH,"//select[@id='id7']"))
country.select_by_visible_text("INDIA")
driver.find_element(By.XPATH,"//input[@id='id6']").send_keys("chennai")
driver.find_element(By.XPATH,"//input[@value='Submit']").click()
errormsg=driver.find_element(By.CSS_SELECTOR,"ul[class='validation'] li:nth-child(2)").text
print(errormsg)

