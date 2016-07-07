#coding:utf-8
from selenium import webdriver
# import time
import sys
from public import login
from public import com
# import go

# 元素定位参数
pub_btn1 = 'document.getElementsByClassName("menu-item-header")[3].click()'			# 首页“发布项目”按钮位置
pub_btn2 = 'document.getElementsByClassName("publish-type-btn")[0].click()'			# 引导页“发布悬赏”按钮位置
pro_cat1 = 'document.getElementsByClassName("ic-project-website")[0].click()'			# 项目类别--网站开发
pro_cat2 = 'document.getElementsByClassName("ic-project-wechat")[0].click()'			# 项目类别--微信开发
pro_cat3 = 'document.getElementsByClassName("ic-project-app")[0].click()'				# 项目类别--移动开发
pro_cat4 = 'document.getElementsByClassName("ic-project-html5")[0].click()'			# 项目类别--html5应用
pro_cat5 = 'document.getElementsByClassName("ic-project-sdkapi")[0].click()'			# 项目类别--SDK/API开发
pro_cat6 = 'document.getElementsByClassName("ic-project-translate")[0].click()'		# 项目类别--文档翻译
pro_cat7 = 'document.getElementsByClassName("ic-project-misc")[0].click()'				# 项目类别--其他
rew_body = u'这是一个悬赏测试'
budget = "100000"
period = "10"
skill = "Java JavaEE JavaSE"


# 1、发布悬赏
def publish_reward(driver, pro_name):
	driver = webdriver.Chrome()
	#发布者登陆
	login.login(driver,'1')
	print(u"发布者登陆成功！")

	driver.get("http://zb.oschina.org/")
	driver.find_element_by_class_name("menu-item").click()

	handle = com.get_window(driver,u"找活首页-开源中国众包平台")
	driver.execute_script(pub_btn1)


	handle = com.get_window(driver, u"发布需求-开源中国众包平台")
	driver.execute_script(pub_btn2)

	# 填写表单
	handle = com.get_window(driver, u"发布悬赏-开源中国众包平台")
	driver.execute_script(pro_cat1)
	driver.find_element_by_id("reward-title").clear()
	driver.find_element_by_id("reward-title").send_keys(pro_name)
	driver.find_element_by_class_name("simditor-body").send_keys(rew_body)
	driver.find_element_by_id("reward-budget").clear()
	driver.find_element_by_id("reward-budget").send_keys(budget)
	driver.find_element_by_id("period").clear()
	driver.find_element_by_id("period").send_keys(period)
	# ckbox = driver.find_element_by_class_name("new-choose-box")	#悬赏模式选择
	# ckbox.find_element_by_id("rd-1").click()
	driver.find_element_by_id("reward-skills").send_keys(skill)
	agree = 'document.getElementsByClassName("choose-box")[4].click()'
	driver.execute_script(agree)
	driver.find_element_by_id("publish-reward-submit").click()
	print(u"发布成功，等待审核！")
	driver.quit()

