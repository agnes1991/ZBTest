#coding:utf-8
from selenium import webdriver
import sys
from public import com


driver = webdriver.Chrome()
driver.maximize_window()

# driver.get("http://www.oschina.org")

driver.get("http://www.oschina.org/home/login?goto_page=http%3A%2F%2Fzb.oschina.org%2F")
driver.find_element_by_id("f_email").clear()
driver.find_element_by_id("f_email").send_keys("rui_huang@outlook.com")
driver.find_element_by_id("f_pwd").clear()
driver.find_element_by_id("f_pwd").send_keys("123456")
sub = driver.find_element_by_class_name("rndbutton")
sub.click()


# div = driver.find_element_by_id("ZB")
# a = div.find_element_by_tag_name("a")
# a.click()

handle = com.get_window(driver, u"开源中国众包平台")
# driver.switch_to_window(handle)


print(handle)
# menu = driver.find_element_by_class_name("menu")
# a_reward = menu.find_element_by_tag_name("a")
# a_reward.click()

