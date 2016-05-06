#coding:utf-8
from selenium import webdriver
import sys
from public import com


driver = webdriver.Firefox()
# driver.maximize_window()

driver.get("https://www.oschina.net")

div = driver.find_element_by_class_name("TodayNews")
p1 = driver.find_element_by_class_name("p1")
a = p1.find_element_by_tag_name("a")
a.click()

handle = com.get_window(driver, u"开源中国众包平台")
# driver.switch_to_window(handle)

aside = driver.find_element_by_tag_name("aside")
rew = aside.find_elements_by_class_name("toolbox")
a1 = rew[0].find_element_by_tag_name("a")
a2 = rew[2].find_element_by_tag_name("a")
print a1,a2
a1.click()
a2.click()

win2 = com.get_window(driver, u"前端二次开发")
# driver.switch_to_window(win2)
date1 = driver.find_element_by_class_name("publish-date")
owner = date1.find_element_by_tag_name("a")
owner.click()
