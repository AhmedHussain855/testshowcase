import selenium
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe",options=options)
time.sleep(3)
driver.get("file:///C:/Users/umars/Downloads/viewForm/viewForm/index.html")
time.sleep(2)
driver.find_element_by_id("name").send_keys("ji kia saab hai ")
time.sleep(2)
driver.find_element_by_id("age").send_keys("31")
time.sleep(2)
driver.find_element_by_id("dob").send_keys("08-08-1983")
time.sleep(2)
driver.find_element_by_id("address").send_keys("173 Cowboys pkwy")
time.sleep(2)
driver.find_element_by_id("Num").send_keys("858-790-2620")
time.sleep(2)
driver.find_element_by_id("button1").click()
time.sleep(2)
driver.find_element_by_id("button2").click()
time.sleep(10)

driver.close()


