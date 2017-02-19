from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import requests, sys, webbrowser, time, os, selenium


def generate_stl(input_text):
    profile = FirefoxProfile()
    profile.set_preference("browser.download.folderList",2)
    profile.set_preference("browser.download.manager.showWhenStarting",False)
    profile.set_preference("browser.download.dir",os.getcwd())
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/vnd.ms-pki.stl')
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.set_window_size(800,600)
    driver.set_window_position(1180, 0)
    driver.get('http://v01pe.github.io/Text2Braille3d/')

    # input text to be printed
    text_form = driver.find_element_by_css_selector('.parameterstable > tr:nth-child(1) > td:nth-child(2) > textarea:nth-child(1)')
    text_form.clear()
    text_form.send_keys(input_text)

    # open advanced options
    advanced_tickbox = driver.find_element_by_css_selector('#more')
    advanced_tickbox.click()

    # disable support circles
    support_option = driver.find_element_by_css_selector('.parameterstable > tr:nth-child(11) > td:nth-child(2) > input:nth-child(1)')
    support_option.click()

    # submit text for rendering
    submit_button = driver.find_element_by_css_selector('.parametersdiv > button:nth-child(5)')
    submit_button.click()

    driver.execute_script("window.scrollTo(0, 40)")

    # generate stl file
    wait = WebDriverWait(driver, 30)
    stl_generate_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.statusdiv > div:nth-child(2) > button:nth-child(4)')))
    #stl_generate_button = driver.find_element_by_css_selector('.statusdiv > div:nth-child(2) > button:nth-child(4)')

    stl_generate_button.click()



    # download stl file
    stl_downlowd_button = driver.find_element_by_css_selector('.statusdiv > div:nth-child(2) > a:nth-child(5)')
    stl_downlowd_button.click()

if __name__ == '__main__':
    generate_stl('python')
