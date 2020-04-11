import selenium
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe",options=options)
time.sleep(3)
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
time.sleep(3)
driver.find_element_by_id("txtUsername").send_keys("Admin")
time.sleep(3)
driver.find_element_by_id("txtPassword").send_keys("admin123")
time.sleep(3)
driver.find_element_by_id("btnLogin").click()
time.sleep(5)

driver.close()







