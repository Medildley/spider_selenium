from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

 
driver = webdriver.Chrome()
driver.get("http://172.17.249.10/NewSys/login.aspx?ReturnUrl=%2fNewSys%2fdefault.aspx")
time.sleep(2)
#用户名 密码  
elem_user = driver.find_element_by_name("TextBoxUserName")  
elem_user.send_keys("qihu") 
elem_pwd = driver.find_element_by_name("TextBoxPassword")  
elem_pwd.send_keys("Timfay1!")
elem_pwd.send_keys(Keys.RETURN) 
time.sleep(2)  
#driver.find_element_by_name("ImageButtonLogin").click()

#日志填写
time.sleep(1)
driver.find_element_by_id("HeaderControl1_HyperLink2").click()

time.sleep(10)#睡5秒来拉验证码


time.sleep(1)
driver.find_element_by_id("__tab_ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderRight_TabContainer_TabPanel3").click()

time.sleep(1)
driver.find_element_by_id("ctl00_ctl00_ContentPlaceHolder1_ContentPlaceHolderRight_TabContainer_TabPanel3_MyReqAssignments_gvLog_ctl05_hplkLog").click()

#根据序号（第一个frame)来定位
driver.switch_to.frame(0)
elem_input = driver.find_element_by_id("ctl00_ContentPlaceHolder1_TextBoxLog")
elem_input.send_keys(Keys.TAB)
elem_input.send_keys("李老师好! ( •̀∀•́ )")

Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_TaskTypeSelect_ddlTaskSubType')).select_by_value("48")
time.sleep(1)
Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_ReqSystemSelect_ddlSystem')).select_by_value("13192")

elem_time = driver.find_element_by_id("ctl00_ContentPlaceHolder1_TextBoxWorkMinutes")
elem_time.send_keys("60")

time.sleep(1)
elem_time.send_keys(Keys.RETURN) 

