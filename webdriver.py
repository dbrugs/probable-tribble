from selenium import webdriver
import atexit

def make_webdriver():
    browser = webdriver.Firefox(executable_path = '/home/brugs_bunny/webdriver/bin/geckodriver')
    atexit.register(lambda: browser.quit())
    return browser
