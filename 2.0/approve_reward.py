# coding:utf-8
from selenium import webdriver
from public import com
from public import login
from selenium.webdriver.common.action_chains import ActionChains
# import go

# driver = webdriver.Chrome()

pro_name = "发布一个悬赏"
# 2、后台审核悬赏
def approve_reward(driver):
	driver = webdriver.Chrome()
	#发布者登陆
	login.login(driver,'3')
	print("登陆成功")

	# 查找到发布的项目
	driver.find_element_by_link_text(u"众包管理").click()
	driver.find_element_by_link_text(u"待审核悬赏").click()
	# srh = 'document.getElementsByName("q").clear()'
	driver.find_element_by_name("q").clear()
	driver.find_element_by_name("q").send_keys(pro_name)
	driver.find_element_by_name("q").submit()

	# 审核项目
	driver.find_element_by_link_text(u"通过").click()

	driver.implicitly_wait(3)
	# driver.switch_to_alert()
	driver.find_element_by_id("update-tag").click()
	print(u"审核通过，待托管！")
	driver.quit()

# 3、托管赏金
def host_reward_budget(driver):
	driver = webdriver.Chrome()
	# 托管赏金
	login.login(driver,'1')
	print(u"发布者登陆成功")

	my_wp = driver.find_element_by_link_text(u"我的工作台")
	ActionChains(driver).move_to_element(my_wp)
	driver.implicitly_wait(3)
	driver.find_elements_by_class_name("glyphicon-menu-down")[1].click()

	handle = com.get_window(driver,u"开源中国众包平台-我的众包 ")
	driver.find_element_by_link_text(u"发布的项目").click()
	driver.find_element_by_link_text(u"进入工作台").click()
	driver.find_element_by_link_text(u"托管赏金").click()
	driver.find_element_by_class_name("notice-confirm").click()

	handle= com.get_window(driver,u"选择订单支付方式-开源中国众包平台")
	driver.find_element_by_id("pay_btn").click()

	handle = com.get_window(driver,u"支付结果-开源中国众包平台")
	driver.find_element_by_link_text(u"查看我的悬赏").click()
	print(u"托管赏金成功！")
	driver.quit()

