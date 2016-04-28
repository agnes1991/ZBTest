#coding:utf-8
from selenium import webdriver
import sys

driver = webdriver.Firefox()

#登陆后台管理
driver.get("http://www.oschina.org/home/login?goto_page=http%3A%2F%2Fadmin.oschina.net%2F")
driver.find_element_by_id("f_email").clear()
driver.find_element_by_id("f_email").send_keys("bei__mu@126.com")
driver.find_element_by_id("f_pwd").clear()
driver.find_element_by_id("f_pwd").send_keys("123456")
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/form/div[2]/table/tbody/tr[7]/td/input").click()
driver.get("http://admin.oschina.org/")

#众包管理
driver.find_element_by_xpath("/html/body/div[1]/div[1]/ul/li[3]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr/td[1]/ul/li[2]/ol/li[1]/a").click()
