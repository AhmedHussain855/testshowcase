import selenium
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome("C:\chromedriver\chromedriver.exe",options=options)
time.sleep(3)
driver.get("https://www.fedex.com/en-us/home.html")
time.sleep(2)
driver.find_element_by_class_name("fxg-header__logo").click()
time.sleep(2)
driver.save_screenshot("C:\Python34\Lib\Screenshort\haider.png")
driver.find_element_by_xpath("//*[@id='fxg-header--sticky']/div/div/div/div[1]/div/ul/div[1]/li/a").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/header/div/div/nav/div/ul/div[2]/li/a/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/header/div/div/nav/div/ul/div[3]/li/a/span").click()
time.sleep(2)
