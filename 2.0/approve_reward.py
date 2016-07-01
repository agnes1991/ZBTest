# coding:utf-8
from selenium import webdriver
from public import com
from public import login

driver = webdriver.Chrome()

#发布者登陆
login.login(driver,'3')
print("登陆成功")

# 查找到发布的项目
driver.find_element_by_link_text(u"众包管理").click()
driver.find_element_by_link_text(u"待审核悬赏").click()
driver.find_element_by_name("q").clear()
driver.find_element_by_name("q").send_keys(u"发布一个悬赏测试全流程")
driver.find_element_by_name("q").submit()

# 审核项目
driver.find_element_by_link_text(u"通过").click()

driver.implicitly_wait(3)

# driver.switch_to_alert()
driver.find_element_by_id("update-tag").click()