# coding:utf-8
from selenium import webdriver
from public import com
from public import login
import time

menu_pro = 'document.getElementsByClassName("menu-item-header")[0].click()'			# “找活”菜单
reg_des = u"我很适合这个项目"
reg_sch = "10"

# print(pro_name)
# 4、报名悬赏项目
def reg_reward(driver,pro_name):
	driver = webdriver.Chrome()
	login.login(driver,'2')
	print(u"报名者登陆成功！")

	driver.execute_script(menu_pro)
	title = pro_name
	# user_title = driver.find_elements_by_class_name("user-title")[1].text
	# print(user_title)
	for i in range (0,9):
		user_title = driver.find_elements_by_class_name("user-title")[i].text
		# print(user_title)
		if title in user_title:
			driver.find_elements_by_class_name("user-title")[i].click()

	pro_name = name + time
	handle_name = pro_name + '-开源中国众包平台'
	handle = com.get_window(driver,handle_name)
	# 收藏
	driver.find_element_by_id("heart").click()
	print(u"收藏成功！")
	# 报名
	driver.find_elements_by_class_name("follow")[1].click()
	driver.find_element_by_id("description").clear()
	driver.find_element_by_id("description").send_keys(reg_des)
	driver.find_element_by_id("scheduled").clear()
	driver.find_element_by_id("scheduled").send_keys(reg_sch)
	driver.find_element_by_class_name("choose-box").click()
	a1 = driver.find_element_by_id("reward-apply")
	a1.find_element_by_class_name("bn").click()
	print("报名成功！")
	driver.quit()
	
