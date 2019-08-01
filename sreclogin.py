from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

def startabrowser(username, password):
	driver = webdriver.Firefox()
	driver.get("http://10.0.0.1:2280/cportal/login.html?h=114e5374&url=http://10.0.0.1/")

	driver.find_element_by_id("usrname").send_keys(username)
	driver.find_element_by_id("newpasswd").send_keys(password)
	driver.find_element_by_id("terms").click()
	driver.find_element_by_id("update_btn").click()
	time.sleep(2)

	driver.close()

if __name__ == "__main__":
	# Change the username and password
	username = "username"
	password = "password"
	startabrowser(username, password)