# coding:utf-8
from selenium import webdriver
from public import com
from public import login

driver = webdriver.Chrome()

#发布者登陆
login.login(driver,'3')
print("登陆成功")

# driver.implicitly_wait(5)
# driver.get("http://admin.oschina.org/")