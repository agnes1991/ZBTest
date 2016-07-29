# coding:utf-8
from selenium import webdriver
from public import com
from public import login
import publish_reward
import approve_reward
import reg_reward
import finish_reward
import time
import rate_reward

driver = webdriver.Chrome()

time_tag = time.strftime('%m%d%H%M',time.localtime(time.time()))
name = u"来自test的悬赏项目"
pro_name = name + time_tag
print(pro_name)


# 1、发布悬赏
publish_reward.publish_reward(driver, pro_name)
driver.implicitly_wait(3)

# 2、后台审核悬赏
approve_reward.approve_reward(driver, pro_name)
driver.implicitly_wait(3)

# 3、托管赏金
approve_reward.host_reward_budget(driver)
driver.implicitly_wait(3)

# 4、报名悬赏项目
reg_reward.reg_reward(driver, pro_name)
driver.implicitly_wait(3)

# 5、审核报名信息通过
finish_reward.confirm_reg(driver)
driver.implicitly_wait(3)

# 6、第一次提交解决方案
finish_reward.sub_solu(driver)
driver.implicitly_wait(3)

# 7、追加赏金
finish_reward.add_budget(driver)
driver.implicitly_wait(3)

# 8、拒绝第一次的解决方案
finish_reward.refuse_solu(driver)
driver.implicitly_wait(3)

# 9、修改解决方案，第二次提交
finish_reward.update_solu(driver)
driver.implicitly_wait(3)

# 10、选为最佳方案
finish_reward.approve_solu(driver)
driver.implicitly_wait(3)

# 11、结赏
finish_reward.finish(driver)
driver.implicitly_wait(3)

# 12、发布者评价开发者
rate_reward.rate_seller(driver)
driver.implicitly_wait(3)

# 13、开发者评价发布者
rate_reward.rate_buyer(driver)
driver.implicitly_wait(3)

driver.quit()