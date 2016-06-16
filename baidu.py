#coding:utf-8
from selenium import webdriver
import sys
from public import com


driver = webdriver.PhantomJS()
driver.maximize_window()

driver.get("https://www.oschina.net")

div = driver.find_element_by_id("ZB")
a = div.find_element_by_tag_name("a")
a.click()

handle = com.get_window(driver, u"开源中国众包平台")
# driver.switch_to_window(handle)

menu = driver.find_element_by_class_name("menu")
a_reward = menu.find_element_by_tag_name("a")
a_reward.click()

