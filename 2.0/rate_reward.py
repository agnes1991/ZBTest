# coding:utf-8
from selenium import webdriver
from public import login
from public import com
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

l1 = "/html/body/div[1]/div/section/article/div/div[2]/table/tbody/tr[1]/td[5]/div[3]/button"		# l1发布者工作台列表“评价”按钮位置
l2 = '//*[@id="rate-form"]/div[3]/button'															# l2提交评价时，“确认提交”按钮位置
l3 = '/html/body/div[1]/div/section/article/div/div[2]/table/tbody/tr[1]/td[6]/div[2]/button'		# l3开发者工作台列表“评价”按钮位置

# 发布者评价开发者
# login.login(driver,'1')
# my_wp = driver.find_element_by_link_text(u"我的工作台")
# ActionChains(driver).move_to_element(my_wp)
# driver.implicitly_wait(3)
# driver.find_elements_by_class_name("glyphicon-menu-down")[1].click()

# handle = com.get_window(driver,u"参与的项目-开源中国众包平台")
# driver.find_element_by_link_text(u"发布的项目").click()

# handle = com.get_window(driver,u"发布的项目-开源中国众包平台")
# driver.find_element_by_xpath(l1).click()
# # 选择评价星级
# r1 = driver.find_element_by_id("corp")
# r1.find_elements_by_tag_name("img")[2].click()
# r2 = driver.find_element_by_id("comm")
# r2.find_elements_by_tag_name("img")[3].click()
# r3 = driver.find_element_by_id("skil")
# r3.find_elements_by_tag_name("img")[3].click()
# r4 = driver.find_element_by_id("qual")
# r4.find_elements_by_tag_name("img")[4].click()
# r5 = driver.find_element_by_id("resp")
# r5.find_elements_by_tag_name("img")[4].click()
# driver.find_element_by_id("comment").clear()
# driver.find_element_by_id("comment").send_keys(u"这是一个评价")
# driver.find_element_by_xpath(l2).click()

# 开发者评价发布者
login.login(driver,'2')
my_wp = driver.find_element_by_link_text(u"我的工作台")
ActionChains(driver).move_to_element(my_wp)
driver.implicitly_wait(3)
driver.find_elements_by_class_name("glyphicon-menu-down")[1].click()

handle = com.get_window(driver,u"参与的项目-开源中国众包平台")
driver.find_element_by_xpath(l3).click()

handle = com.get_window(driver,u"评价对方-开源中国众包平台")
r1 = driver.find_element_by_id("corp")
r1.find_elements_by_tag_name("img")[2].click()
r2 = driver.find_element_by_id("comm")
r2.find_elements_by_tag_name("img")[3].click()
r3 = driver.find_element_by_id("paym")
r3.find_elements_by_tag_name("img")[3].click()
r4 = driver.find_element_by_id("requ")
r4.find_elements_by_tag_name("img")[4].click()
r5 = driver.find_element_by_id("resp")
r5.find_elements_by_tag_name("img")[4].click()
driver.find_element_by_id("comment").clear()
driver.find_element_by_id("comment").send_keys(u"这是一个评价")
driver.find_element_by_xpath(l2).click()