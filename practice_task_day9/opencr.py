import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

today = date.today()
print("Today's date:", today)
d1 = today.strftime("%Y-%m-%d")
print("d1 =", d1)
driver = webdriver.Chrome()
driver.get('http://demo.openemr.io/b/openemr/')
driver.maximize_window()
driver.find_element(By.XPATH,("//input[@id='authUser']")).send_keys("admin")
driver.find_element(By.XPATH,"//input[@id='clearPass']").send_keys("pass")
language=Select(driver.find_element(By.XPATH,('//select[@name="languageChoice"]')))
language.select_by_value("18")
driver.find_element(By.XPATH,("//button[@id='login-button']")).click()
wait=WebDriverWait(driver,20)
# menubtn=wait.until(Ec.visibility_of_element_located(((By.XPATH,"//div[@id='mainBox']/nav[1]/button[1]/span[1]"))))
# menubtn.click()
action = webdriver.ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,("(//div[contains(text(),'Patient')])[1]"))).perform()
driver.find_element(By.XPATH,("//div[contains(text(),'New/Search')]")).click()
wait.until(Ec.frame_to_be_available_and_switch_to_it(((driver.find_element(By.XPATH,"//iframe[@name='pat']")))))
title=Select(driver.find_element(By.XPATH,"//select[@id='form_title']"))
title.select_by_visible_text("Mr.")
driver.find_element(By.XPATH,("//input[@id='form_fname']"))
driver.find_element(By.XPATH,("//input[@id='form_fname']")).send_keys("Jack")
driver.find_element(By.XPATH,("//input[@id='form_lname']")).send_keys("Sparrow")
driver.find_element(By.CSS_SELECTOR,"#form_DOB").send_keys(d1)
sex=Select(driver.find_element(By.CSS_SELECTOR,"#form_sex"))
sex.select_by_visible_text("Male")
driver.find_element(By.CSS_SELECTOR,"#create").click()
driver.switch_to.default_content()
wait.until(Ec.frame_to_be_available_and_switch_to_it(((driver.find_element(By.XPATH,"//iframe[@id='modalframe']")))))
driver.find_element(By.CSS_SELECTOR,"input[value='Confirm Create New Patient']").click()
driver.switch_to.default_content()
alert=wait.until(Ec.alert_is_present())
alertmsg=alert.text
print("Alerttext:",alertmsg)
alert.accept()
popup=driver.find_element(By.XPATH, "(//div[@class='closeDlgIframe'])[1]").is_displayed()
print(popup)
if popup==True:
    driver.find_element(By.XPATH, "(//div[@class='closeDlgIframe'])[1]").click()
# driver.find_element(By.XPATH,"(//div[@class='closeDlgIframe'])[1]").click()
Patient_name=driver.find_element(By.XPATH,"(//span[@data-bind='text: pname()'])[1]")
Patient_name.click()
print("Patient name is:",Patient_name.text)
time.sleep(5)

