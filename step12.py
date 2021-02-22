from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_css_selector("[name='firstname']")
    name.send_keys("Arina")
    lastName = browser.find_element_by_css_selector('[name="lastname"]')
    lastName.send_keys("Kamliuk")
    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys('hgvkhg')

    file = browser.find_element_by_id("file")
    file.send_keys("C:/Phyton/Arina/stepik/step.txt")

    button = browser.find_element_by_css_selector("[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()