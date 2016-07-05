#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# 获取页面句柄
def get_window(driver,title):
	for handle in driver.window_handles:
		driver.switch_to_window(handle)
		if title in driver.title:
			return handle


# 评价星级
def rate_buyer(driver,star1,star2,star3,star4,star5):
	star1 = range_fix(star1)
	star2 = range_fix(star2)
	star3 = range_fix(star3)
	star4 = range_fix(star4)
	star5 = range_fix(star5)

	r1 = driver.find_element_by_id("corp")
	r1.find_elements_by_tag_name("img")[2].click()
	r2 = driver.find_element_by_id("comm")
	r2.find_elements_by_tag_name("img")[3].click()
	r3 = driver.find_element_by_id("skil")
	r3.find_elements_by_tag_name("img")[3].click()
	r4 = driver.find_element_by_id("qual")
	r4.find_elements_by_tag_name("img")[4].click()
	r5 = driver.find_element_by_id("resp")
	r5.find_elements_by_tag_name("img")[4].click()

def rate_seller(driver,star1,star2,star3,star4,star5):
	star1 = range_fix(star1)
	star2 = range_fix(star2)
	star3 = range_fix(star3)
	star4 = range_fix(star4)
	star5 = range_fix(star5)

	r1 = driver.find_element_by_id("corp")
	r1.find_elements_by_tag_name("img")[star1].click()
	r2 = driver.find_element_by_id("comm")
	r2.find_elements_by_tag_name("img")[star2].click()
	r3 = driver.find_element_by_id("paym")
	r3.find_elements_by_tag_name("img")[star3].click()
	r4 = driver.find_element_by_id("requ")
	r4.find_elements_by_tag_name("img")[star4].click()
	r5 = driver.find_element_by_id("resp")
	r5.find_elements_by_tag_name("img")[star5].click()

# 评价星级判断
def range_fix(star):
	if star>4:
		star=4
	elif star<0:
		star=0
	return star

# 发布者进入工作台列表
def goto_wp(driver):
	my_wp = driver.find_element_by_link_text(u"我的工作台")
	ActionChains(driver).move_to_element(my_wp)
	driver.implicitly_wait(3)
	driver.find_elements_by_class_name("glyphicon-menu-down")[1].click()

# 支付页面
def pay_page(driver):
	handle = get_window(driver,u"选择订单支付方式-开源中国众包平台")
	driver.find_element_by_id("pay_btn").click()
