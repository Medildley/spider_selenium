from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() # Get local session of chrome 
driver.get("https://passport.jd.com/new/login.aspx")
time.sleep(3)

elem_account = driver.find_element_by_name("loginname")
elem_password = driver.find_element_by_name("nloginpwd")
elem_account.clear()
elem_password.clear()
elem_account.send_keys("abc")
elem_password.send_keys("123")
driver.find_element_by_id("loginsubmit").click()

