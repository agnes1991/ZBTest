#coding:utf-8
from selenium import webdriver

def switch_to_window (page,all_handles):
	all_handles = driver.window_handles

	for handle in all_handles:
	if handle == home_page:
		driver.switch_to_window(handle)