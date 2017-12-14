from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

#open url
driver = webdriver.Chrome() # Get local session of chrome 
driver.get("http://mail.163.com") # Load page
time.sleep(2)  

driver.switch_to_frame('x-URS-iframe') 
elem_user = driver.find_element_by_name("email")
elem_user.send_keys("abc@163.com")  
time.sleep(1) 
elem_pwd = driver.find_element_by_name("password")  
elem_pwd.send_keys("123")  
elem_pwd.send_keys(Keys.RETURN)
time.sleep(2) 
driver.find_element_by_id("_mail_component_66_66").click() 
time.sleep(1) 
#elem_recv = driver.find_element_by_class_name(".js-component-emailtips.nui-ipt-placeholder") 
#elem_recv.send_keys("598643132@qq.com")  

time.sleep(5) 
#driver.close()  
#driver.quit()  
