# coding:utf-8
from selenium import webdriver
from public import com
from public import login
from selenium.webdriver.common.action_chains import ActionChains
import time
# import go

zb_m = '//*[@id="Modules"]/li[3]/a'								# “众包管理”菜单   /html/body/div[1]/div[1]/ul/li[3]/a
approve_rew = '//*[@id="OMS_Menu"]/ul/li[3]/ol/li[1]/a'						# “待审核悬赏”菜单
confirm = '/html/body/div[1]/div[2]/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td[10]/a[1]'		# “通过”悬赏链接
pubed_pro = '/html/body/div[1]/div/section/nav/div/div[2]/div/a[2]'								# “发布的项目”菜单
wp = '/html/body/div[1]/div/section/article/div/div[2]/table/tbody/tr[1]/td[5]/div[1]/a'		# 工作台项目列表，第一个项目的“进入工作台”链接
host_btn = 'document.getElementsByClassName("bn-icon")[0].click()'								# “托管赏金”按钮


# print(pro_name)
# 2、后台审核悬赏
def approve_reward(driver, pro_name):
	driver = webdriver.Chrome()
	#发布者登陆
	login.login(driver,'3')
	print("登陆成功")
	handle = com.get_window(driver,u'首页 - OSC业务管理系统')
	# print(handle)
	driver.implicitly_wait(3)

	# 查找到发布的项目
	driver.find_element_by_xpath(zb_m).click()
	driver.find_element_by_xpath(approve_rew).click()
	# srh = 'document.getElementsByName("q").clear()'
	driver.find_element_by_name("q").clear()
	# pro_name = name+time
	driver.find_element_by_name("q").send_keys(pro_name)
	driver.find_element_by_name("q").submit()
	driver.implicitly_wait(3)

	# 审核项目
	driver.find_element_by_xpath(confirm).click()

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

	com.goto_wp(driver)

	handle = com.get_window(driver,u"开源中国众包平台-我的众包 ")
	driver.find_element_by_xpath(pubed_pro).click()
	driver.find_element_by_xpath(wp).click()
	driver.execute_script(host_btn)
	driver.find_element_by_class_name("notice-confirm").click()

	handle= com.get_window(driver,u"选择订单支付方式-开源中国众包平台")
	driver.find_element_by_id("pay_btn").click()

	handle = com.get_window(driver,u"支付结果-开源中国众包平台")
	driver.find_element_by_link_text(u"查看我的悬赏").click()
	print(u"托管赏金成功！")
	# driver.quit()

