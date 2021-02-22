from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('[type="submit"]').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    chislo = browser.find_element_by_id("input_value")
    x = int(chislo.text)
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    cnopka = browser.find_element_by_css_selector('[type="submit"]')
    cnopka.click()

finally:
    time.sleep(10)
    browser.quit()