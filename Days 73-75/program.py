from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

user = os.getenv('pyBites_USER')
pw = os.getenv('pyBites_PW')

driver = webdriver.Chrome()
driver.get("https://pyplanet.herokuapp.com/")
assert "PyBites 100 Days of Django" in driver.title
elem = driver.find_element_by_link_text('PyPlanet Article Sharer App')
elem.click()
assert "Title" in driver.find_element_by_css_selector('.pure-table thead tr th').text
table_rows = driver.find_elements_by_css_selector('tbody tr') 
assert 100 == len(table_rows)
article_title = driver.find_element_by_css_selector('tbody tr:nth-of-type(3) td a')
time.sleep(2)
article_title.click()
time.sleep(2)
go_back = driver.find_element_by_link_text('Go back')
time.sleep(1)
go_back.click()
time.sleep(2)
assert "PyBites 100 Days of Django" in driver.title
login = driver.find_element_by_link_text('Login')
login.click()
time.sleep(2)
driver.find_element_by_name('username').send_keys(user)
driver.find_element_by_name('password').send_keys(pw + Keys.RETURN)
time.sleep(2)
assert "PyBites 100 Days of Django" in driver.title
login_elem = driver.find_element_by_xpath("//div[@id='login']")
login_text = driver.execute_script('return arguments[0].childNodes[0].nodeValue.trim()', login_elem)
assert 'Welcome back, guest!' in login_text
assert driver.find_element_by_link_text('Logout') != None
elem = driver.find_element_by_link_text('PyPlanet Article Sharer App')
elem.click()
time.sleep(2)
article_title = driver.find_element_by_css_selector('tbody tr:nth-of-type(3) td a')
article_title.click()
time.sleep(2)
assert 'Tweet this' in driver.page_source
logout_elem = driver.find_element_by_link_text('Logout')
logout_elem.click()
time.sleep(2)
assert 'See you!' in driver.page_source
time.sleep(2)
driver.close()

