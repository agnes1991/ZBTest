# coding:utf-8
from selenium import webdriver
from public import login
from public import com
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

# driver = webdriver.Chrome()

# 依靠xpath定位的元素
l1 = "/html/body/div[1]/div/section/article/div/div[2]/table/tbody/tr[1]/td[5]/div[1]/a"	# l1发布项目列表的第一个项目的“进入工作台”位置
# l2 = '//*[@id="apply-btn-2615"]'															# l2报名列表第一个开发者“通过审核”按钮位置
l3 = "/html/body/div[1]/div/section/article/div/div[2]/table/tbody/tr[1]/td[6]/div[1]/a"	# l3参与者参与项目，第一个项目的“进入工作台”位置
l4 = '//*[@id="solution-form"]/article/div[5]/button'										# l4提交解决方案按钮位置
# l5 = '//*[@id="refuse-form-407"]/div[2]/form/div[2]/button'									# l5发布者拒绝方案的“确定拒绝”按钮位置
l6 = '//*[@id="add_advan_area"]/div/div/div/div[4]/div/button[2]'							# l6追加赏金弹窗的“提交”按钮位置
l7 = '//*[@id="solution-update-form"]/article/div[5]/button'								# l7修改解决方案时，“确定修改”按钮位置
# l8 = '//*[@id="refuse-solution-btn-407"]'													# l8将第一个方案选为最佳方案的“最佳方案”按钮位置
# l9 = '//*[@id="best-form-407"]/div[2]/form/div[3]/button'									# l9选为最佳方案时，“确认选择”按钮位置
l10 = '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/a'									# l10最佳方案未支付时，“继续支付”按钮位置

# 5、审核报名信息通过
def confirm_reg(driver):
	driver = webdriver.Chrome()
	login.login(driver,'1')
	print(u"发布者登陆成功！")

	# 发布者审核报名
	com.goto_wp(driver)

	handle = com.get_window(driver,u"参与的项目-开源中国众包平台")
	driver.find_element_by_link_text(u"发布的项目").click()
	driver.find_element_by_xpath(l1).click()

	handle = com.get_window(driver,u"悬赏详情-开源中国众包平台")
	driver.find_element_by_link_text(u"查看报名情况").click()
	driver.implicitly_wait(2)
	confirm = 'document.getElementsByClassName("operate-btn")[2].click()'
	driver.execute_script(confirm)
	print(u"审核通过，关闭报名，进入开发阶段！")
	driver.quit()

# 6、第一次提交解决方案
def sub_solu(driver):
	driver = webdriver.Chrome()
	# 报名者提交方案
	login.login(driver,'2')
	com.goto_wp(driver)

	# 填写解决方案
	handle = com.get_window(driver,u"参与的项目-开源中国众包平台")
	driver.find_element_by_xpath(l3).click()
	driver.find_element_by_id("btn-sub-solution").click()
	driver.find_element_by_id("solution-description").clear()
	driver.find_element_by_id("solution-description").send_keys(u"这是一个解决方案")
	driver.find_element_by_id("solution-source").clear()
	driver.find_element_by_id("solution-source").send_keys("htt://www.bing.com")
	driver.find_element_by_xpath(l4).click()
	print(u"提交解决方案成功！")
	driver.quit()

# 7、追加赏金
def add_budget(driver):
	driver = webdriver.Chrome()
	# 发布者审核提交的解决方案
	login.login(driver,'1')
	com.goto_wp(driver)

	# 追加赏金
	handle = com.get_window(driver,u"参与的项目-开源中国众包平台")
	driver.find_element_by_link_text(u"发布的项目").click()
	driver.find_element_by_xpath(l1).click()
	driver.find_element_by_link_text(u"追加赏金").click()
	driver.find_element_by_class_name("z-input-text").clear()
	driver.find_element_by_class_name("z-input-text").send_keys("10000")
	driver.find_element_by_xpath(l6).click()
	driver.find_element_by_class_name("notice-confirm").click()

	com.pay_page(driver)
	# handle = com.get_window(driver,u"选择订单支付方式-开源中国众包平台")
	# driver.find_element_by_id("pay_btn").click()
	driver.quit()

# 8、拒绝第一次的解决方案
def refuse_solu(driver):
	driver = webdriver.Chrome()
	# 审核解决方案
	handle = com.get_window(driver,u"支付结果-开源中国众包平台")
	driver.find_element_by_link_text(u"查看我的悬赏").click()

	handle = com.get_window(driver,u"悬赏详情-开源中国众包平台")
	ref_solu = 'document.getElementsByClassName("operate-btn")[0].click()'
	driver.execute_script(ref_solu)
	driver.find_element_by_class_name("z-input-textarea").clear()
	driver.find_element_by_class_name("z-input-textarea").send_keys(u"请修改一下解决方案，并再次提交！")
	submit = 'document.getElementsByTagName("button")[0].click()'
	driver.execute_script(submit)
	driver.find_element_by_class_name("notice-confirm").click()
	driver.quit()

# 9、修改解决方案，第二次提交
def update_solu(driver):
	driver = webdriver.Chrome()
	# 开发者修改方案并再次提交
	login.login(driver,'2')
	com.goto_wp(driver)

	handle = com.get_window(driver,u"参与的项目-开源中国众包平台")
	driver.find_element_by_xpath(l3).click()
	driver.find_element_by_id("btn-update-solution").click()
	driver.find_element_by_id("update-solution-description").clear()
	driver.find_element_by_id("update-solution-description").send_keys(u"这是修改后重新提交的解决方案！")
	driver.find_element_by_id("update-solution-source").clear()
	driver.find_element_by_id("update-solution-source").send_keys("http://www.microsoft.com")
	driver.find_element_by_xpath(l7).click()
	print(u"修改方案成功！")
	driver.quit()

# 10、选为最佳方案
def approve_solu(driver):
	driver = webdriver.Chrome()
	# 发布者审核方案并选为最佳方案
	login.login(driver,'1')
	com.goto_wp(driver)

	handle = com.get_window(driver,u"参与的项目-开源中国众包平台")
	driver.find_element_by_link_text(u"发布的项目").click()

	handle = com.get_window(driver,u"发布的项目-开源中国众包平台")
	driver.find_element_by_xpath(l1).click()

	handle = com.get_window(driver,u"悬赏详情-开源中国众包平台")
	# 调试用.继续支付按钮
	# driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/a").click()
	best_solu = 'document.getElementsByClassName("operate-btn")[1].click()'
	driver.execute_script(best_solu)
	driver.find_element_by_id("choose_reason").clear()
	driver.find_element_by_id("choose_reason").send_keys(u"这个是最佳方案！")
	submit_best = 'document.getElementsByTagName("button")[1].click()'
	driver.execute_script(submit_best)
	driver.find_element_by_class_name("notice-confirm").click()
	print(u"最佳方案选定！")
	driver.quit()

# 11、结赏
def finish(driver):
	driver = webdriver.Chrome()
	# driver.find_element_by_xpath(l10).click()
	# 发布者结赏
	com.pay_page(driver)
	# handle = com.get_window(driver,u"选择订单支付方式-开源中国众包平台")
	# driver.find_element_by_id("pay_btn").click()
	driver.find_element_by_class_name("notice-confirm").click()
	print(u"赏金支付成功！")
	driver.quit()