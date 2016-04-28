#coding:utf-8
from selenium import webdriver

# driver = webdriver.Firefox()

def login(driver,role):
	if role == '1':
		email = 'huangrui@oschina.cn'	#发布者
	elif role =='2':
		email = 'selenium@126.com'	#报名者
	else:
		email = 'bei__mu@126.com'	#管理员


	pwd = '123456'

	driver.get("http://www.oschina.org/home/login?goto_page=http%3A%2F%2Fzb.oschina.org%2F")
	driver.find_element_by_id("f_email").clear()
	driver.find_element_by_id("f_email").send_keys(email)
	driver.find_element_by_id("f_pwd").clear()
	driver.find_element_by_id("f_pwd").send_keys(pwd)
	driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/form/div[2]/table/tbody/tr[7]/td/input").click()