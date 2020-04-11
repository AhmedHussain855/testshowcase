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

orangebucket= driver.title
print(orangebucket)



time.sleep(5)
driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_pim_viewPimModule']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_leave_viewLeaveModule']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_time_viewTimeModule']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_recruitment_viewRecruitmentModule']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_Performance_viewPimModule']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_Dashboard_viewPimModule']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_Directory_viewPimModule']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_Maintenance_viewPimModule']/b").click()
time.sleep(4)

driver.close()










