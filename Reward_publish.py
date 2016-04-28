#coding:utf-8
from selenium import webdriver
# import time
import sys
from public import login
from selenium.webdriver.common.action_chains import ActionChains
# import os


driver = webdriver.Firefox()
# driver.maximize_window()

#登陆
login.login(driver,'1')
print "登陆成功"

#进入悬赏
driver.get("http://zb.oschina.org/")
driver.find_element_by_xpath("/html/body/header/div[3]/div/div[2]/div/div/a[1]").click()

#发布悬赏
driver.get("http://zb.oschina.org/reward")
driver.find_element_by_xpath("/html/body/header/div[3]/div/div[2]/div/a").click()

#悬赏类型
driver.find_element_by_id("reward-type").click()
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[1]/div[1]/div[2]/div[1]/div/div[1]").click()

# 悬赏标题
driver.find_element_by_id("reward-title").clear()
driver.find_element_by_id("reward-title").send_keys(u"悬赏自动化测试")

# 悬赏说明
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[1]/div[3]/div[2]/div[2]/div[1]/div[3]").clear()
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[1]/div[3]/div[2]/div[1]/button").click()

# 预算
driver.find_element_by_id("reward-budget").clear()
driver.find_element_by_id("reward-budget").send_keys("10000")

# 悬赏周期
driver.find_element_by_id("period").clear()
driver.find_element_by_id("period").send_keys("3")

# 赏金分配模式
above = driver.find_element_by_id("reward-alloc-type")
ActionChains(driver).move_to_element(above).perform()
# driver.find_element_by_id("reward-alloc-type").click()
# driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[2]/div[3]/div[2]/div[1]/i").click()
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[2]/div[3]/div[2]/div[1]/div/div[4]").click()

# 技能要求
driver.find_element_by_id("reward-skills").clear()
driver.find_element_by_id("reward-skills").send_keys("Python")

# 附件

# 只允许报名通过用户可见(不选则为访客可见)
# driver.find_element_by_id("file_access_perm").click()

# 报名要求

# 同意协议
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[4]/div[5]/div/div/label").click()

print "填写悬赏信息完成"

# 保存草稿
# driver.find_element_by_id("save-reward-draft").click()
# print "保存悬赏成功"

# 发布悬赏
driver.find_element_by_id("publish-reward-submit").click()
print "发布悬赏"

driver.quit()

