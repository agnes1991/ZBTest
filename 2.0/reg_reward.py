# coding:utf-8
from selenium import webdriver
from public import com
from public import login

# driver = webdriver.Chrome()

# 4、报名悬赏项目
def reg_reward(driver):
	login.login(driver,'2')
	print(u"报名者登陆成功！")

	driver.find_element_by_link_text(u"找活").click()
	title = "发布一个悬赏测试全流程"
	# user_title = driver.find_elements_by_class_name("user-title")[1].text
	# print(user_title)
	for i in range (0,9):
		user_title = driver.find_elements_by_class_name("user-title")[i].text
		# print(user_title)
		if title in user_title:
			driver.find_elements_by_class_name("user-title")[i].click()

	handle = com.get_window(driver,u"发布一个悬赏测试全流程-开源中国众包平台")
	# 收藏
	driver.find_element_by_id("heart").click()
	print(u"收藏成功！")
	# 报名
	driver.find_elements_by_class_name("follow")[1].click()
	driver.find_element_by_id("description").clear()
	driver.find_element_by_id("description").send_keys(u"我很适合这个项目")
	driver.find_element_by_id("scheduled").clear()
	driver.find_element_by_id("scheduled").send_keys("10")
	driver.find_element_by_class_name("choose-box").click()
	a1 = driver.find_element_by_id("reward-apply")
	a1.find_element_by_class_name("bn").click()
	print("报名成功！")
