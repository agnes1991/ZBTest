#coding:utf-8
from selenium import webdriver
# import time
import sys
from public import login
from public import com

driver = webdriver.Chrome()

#登陆
login.login(driver,'1')
print "登陆成功"

handle = com.get_window(driver,  u"开源中国众包平台")
# driver.switch_to_window(handle)
print handle

driver.find_element_by_xpath("/html/body/header/div[3]/div/div[2]/div/div[1]/div[1]/a").click()
# projects.click()