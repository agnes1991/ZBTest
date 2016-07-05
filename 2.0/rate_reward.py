# coding:utf-8
from selenium import webdriver
from public import login
from public import com
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome()

l1 = "/html/body/div[1]/div/section/article/div/div[2]/table/tbody/tr[1]/td[5]/div[3]/button"		# l1发布者工作台列表“评价”按钮位置
l2 = '//*[@id="rate-form"]/div[3]/button'															# l2提交评价时，“确认提交”按钮位置
l3 = '/html/body/div[1]/div/section/article/div/div[2]/table/tbody/tr[1]/td[6]/div[2]/button'		# l3开发者工作台列表“评价”按钮位置

# 12、发布者评价开发者
def rate_seller(driver):
	driver = webdriver.Chrome()
	# 发布者评价开发者
	login.login(driver,'1')
	com.goto_wp(driver)
	

	handle = com.get_window(driver,u"参与的项目-开源中国众包平台")
	driver.find_element_by_link_text(u"发布的项目").click()

	handle = com.get_window(driver,u"发布的项目-开源中国众包平台")
	driver.find_element_by_xpath(l1).click()
	# 选择评价星级
	com.rate_buyer(driver,1,2,3,4,5)
	driver.find_element_by_id("comment").clear()
	driver.find_element_by_id("comment").send_keys(u"这是一个评价")
	driver.find_element_by_xpath(l2).click()
	driver.quit()

# 13、开发者评价发布者
def rate_buyer(driver):
	driver = webdriver.Chrome()
	# 开发者评价发布者
	login.login(driver,'2')
	com.goto_wp(driver)

	handle = com.get_window(driver,u"参与的项目-开源中国众包平台")
	driver.find_element_by_xpath(l3).click()

	handle = com.get_window(driver,u"评价对方-开源中国众包平台")
	com.rate_seller(driver,1,2,3,4,5)
	driver.find_element_by_id("comment").clear()
	driver.find_element_by_id("comment").send_keys(u"这是一个评价")
	driver.find_element_by_xpath(l2).click()
	driver.quit()