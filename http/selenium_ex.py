from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get("https://lbjcrs.ust.hk/primo/authen.php")
time.sleep(10)
username = browser.find_element_by_id("extpatid")
password = browser.find_element_by_id("extpatpw")
username.send_keys("username")
password.send_keys("password")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()