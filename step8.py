from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    sait = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(sait)


    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    otvet = browser.find_element_by_id("answer")
    otvet.send_keys(y)

    neRobot = browser.find_element_by_css_selector("[for='robotCheckbox']")
    neRobot.click()
    robot = browser.find_element_by_css_selector("[for='robotsRule']")
    robot.click()
    knopka = browser.find_element_by_css_selector("[type='submit']")
    knopka.click()

finally:
    time.sleep(10)
    browser.quit()
