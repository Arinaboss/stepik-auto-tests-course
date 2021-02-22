from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    chislo = browser.find_element_by_id("input_value")
    x = int(chislo.text)
    y = calc(x)

    stroka = browser.find_element_by_id("answer")
    stroka.send_keys(y)

    robot = browser.find_element_by_css_selector(
        "[for='robotCheckbox']").click()

    rule = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rule)
    rule.click()


    button = browser.find_element_by_css_selector("[type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()

