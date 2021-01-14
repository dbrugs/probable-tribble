from selenium import webdriver
import atexit

def make_webdriver():
    browser = webdriver.Firefox(executable_path = 'pathtodriver')
    atexit.register(lambda: browser.quit())
    return browser
