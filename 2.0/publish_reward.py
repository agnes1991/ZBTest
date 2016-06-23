#coding:utf-8
from selenium import webdriver
import time
import sys
from public import login
from public import com

driver = webdriver.Chrome()

#登陆
login.login(driver,'1')
print "登陆成功"


# all_handle = driver.window_handles
# home_page = driver.current_window_handle
# driver.switch_to_window(home_page)
# print home_page
# # print title

driver.get("http://zb.oschina.org/")
driver.find_element_by_class_name("menu-item").click()

handle = com.get_window(driver,u"找活首页-开源中国众包平台")
driver.find_element_by_link_text(u"发布项目").click()


handle = com.get_window(driver, u"发布需求-开源中国众包平台")
# driver.find_element_by_link_text(u"发布悬赏").click()
driver.find_element_by_xpath("/html/body/section/section/section/a[1]/article/div").click()

handle = com.get_window(driver, u"发布悬赏-开源中国众包平台")
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[4]/form/div[2]/div[2]/div[1]/a[1]/div[1]").click()
driver.find_element_by_id("reward-title").clear()
driver.find_element_by_id("reward-title").send_keys(u"发布一个悬赏测试全流程")
driver.find_element_by_class_name("simditor-body").send_keys(u"这是一个悬赏测试")
driver.find_element_by_id("reward-budget").clear()
driver.find_element_by_id("reward-budget").send_keys("10000")
driver.find_element_by_id("period").clear()
driver.find_element_by_id("period").send_keys("10")
ckbox = driver.find_element_by_class_name("new-choose-box")
ckbox.find_element_by_id("rd-1").click()
driver.find_element_by_id("reward-skills").send_keys("JAVA")
driver.find_element_by_name("agreement").click()