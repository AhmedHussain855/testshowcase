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
driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b").click()
time.sleep(2)
Orangebucket=driver.title
assert driver.title

driver.save_screenshot("C:\Python34\Lib\screenshort\muaz.png")

driver.find_element_by_xpath("//*[@id='menu_dashboard_index']/b").click()

time.sleep(1)
driver.find_element_by_xpath("//*[@id='menu_pim_viewPimModule']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_leave_viewLeaveModule']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_time_viewTimeModule']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_recruitment_viewRecruitmentModule']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu__Performance']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_dashboard_index']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_directory_viewDirectory']/b").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='menu_maintenance_purgeEmployee']/b").click()
time.sleep(4)
driver.find_element_by_id("welcome").click()
time.sleep(1)
driver.find_element_by_link_text("Logout").click()

time.sleep(1)

driver.close()

print("my scripts successfully Completed ")










