from selenium import webdriver
import time

try:
    link = " http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    button = browser.find_element_by_id("button").click()

finally:
    time.sleep(10)
    browser.quit()

