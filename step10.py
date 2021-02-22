from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    fisrt_number = browser.find_element_by_id("num1")
    x = int(fisrt_number.text)

    second_number = browser.find_element_by_id("num2")
    y = int(second_number.text)

    chislo = x + y
    otvet = str(chislo)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(otvet)

    knopka = browser.find_element_by_css_selector("[type='submit']")
    knopka.click()



finally:
    time.sleep(10)
    browser.quit()





