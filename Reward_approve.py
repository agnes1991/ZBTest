#coding:utf-8
from selenium import webdriver
import sys
from public import login
import time

driver = webdriver.Firefox()

#登陆后台管理
login.login(driver,'3')
print "登陆成功"

driver.implicitly_wait(3)

driver.get("http://admin.oschina.org")
#众包管理
driver.find_element_by_xpath("/html/body/div[1]/div[1]/ul/li[3]/a").click()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr/td[1]/ul/li[2]/ol/li[1]/a").click()

#查询到发布的悬赏
driver.find_element_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div/h2/form/input[1]").clear()
driver.find_element_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div/h2/form/input[1]").send_keys(u"悬赏自动化测试")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div/h2/form/input[2]").submit()

#审核通过
driver.find_element_by_xpath("/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td[8]/a[1]").click()
driver.switch_to_alert().accept()
print "悬赏通过审核"

# driver.quit()