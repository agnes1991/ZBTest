#coding:utf-8
from selenium import webdriver

def get_window(driver,title):
	for handle in driver.window_handles:
		driver.switch_to_window(handle)
		if title in driver.title:
			return handle
