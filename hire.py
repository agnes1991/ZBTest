#coding:utf-8
from selenium import webdriver
import sys
from public import login
# from public import pub

driver = webdriver.Firefox()
# driver.maximize_window()

#登陆
login.login(driver,'1')
print "登陆成功"



all_handles = driver.window_handles
home_page = driver.current_window_handle


for handle in all_handles:
	if handle == home_page:
		driver.find_element_by_link_text(u"找人").click()

hire_page = driver.current_window_handle

for handle in all_handles:
	if handle == hire_page:
		driver.find_element_by_link_text(u"兼职项目").click()
		driver.switch_to_window(handle)
for handle in all_handles:
	if handle == 
driver.find_element_by_xpath("/html/body/header/div[3]/div/div[2]/div/a").click()

new_hire = driver.current_window_handle

for handle in all_handles:
	if handle == new_hire:
		driver.switch_to_window(new_hire)

# 项目类型
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[1]/div[1]/div[2]/div/i").click()
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[1]/div[1]/div[2]/div/div/div[1]").click()
# 标题
driver.find_element_by_id("project-title").clear()
driver.find_element_by_id("project-title").send_keys("兼职项目测试——test")
# 描述
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[1]/div[3]/div[2]/div[2]/div[1]/div[3]").clear()
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[1]/div[3]/div[2]/div[1]/button[1]").click()
# 金额，日薪和周期
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[2]/div[1]/div/div[2]/div[1]/i").click()
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[2]/div[1]/div/div[2]/div[1]/div/div[2]").click()
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[2]/div[1]/div/div[2]/div[2]/i").click()
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[2]/div[1]/div/div[2]/div[2]/div/div[3]").click()
# 工作模式
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[2]/div[2]/div[2]/div/div/div/div[1]/label").click()
# 技能要求
driver.find_element_by_id("project-skills").clear()
driver.find_element_by_id("project-skills").send_keys("Java")
# 项目附件
# 手机号码
# 邮箱
# 发布
driver.find_element_by_xpath("/html/body/div[2]/div/section/div[2]/section/article/fieldset[3]/div[5]/div/div/label").click()
# 保存草稿
driver.find_element_by_xpath("save-hire-draft").click()
# 发布项目
driver.find_element_by_id("publish-hire-submit").click()

driver.quit()