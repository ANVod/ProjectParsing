from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
time.sleep(10)
browser.quit()
