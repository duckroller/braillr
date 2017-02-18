from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import requests, sys, webbrowser, bs4, time

#content_type = requests.head('http://v01pe.github.io/6e7f89b1-94ad-403e-815d-f3b93fd0ec8b').headers['content-type']
#print(content_type)

profile = FirefoxProfile()
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/sla')
driver = webdriver.Firefox()#firefox_profile=profile)
driver.get('http://v01pe.github.io/Text2Braille3d/')

text_form = driver.find_element_by_css_selector('.parameterstable > tr:nth-child(1) > td:nth-child(2) > textarea:nth-child(1)')

text_form.clear()
text_form.send_keys("python")

submit_button = driver.find_element_by_css_selector('.parametersdiv > button:nth-child(5)')

submit_button.click()

time.sleep(20)

stl_generate_button = driver.find_element_by_css_selector('.statusdiv > div:nth-child(2) > button:nth-child(4)')

stl_generate_button.click()

stl_downlowd_button = driver.find_element_by_css_selector('.statusdiv > div:nth-child(2) > a:nth-child(5)')

stl_downlowd_button.click()
