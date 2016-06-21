#coding:utf-8
from selenium import webdriver
# import time
import sys
from public import login

driver = driver = webdriver.Firefox()

#登陆
login.login(driver,'1')
print "登陆成功"