from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id("book").click()

    chislo = browser.find_element_by_id("input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", chislo)
    x = int(chislo.text)
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    knopka = browser.find_element_by_id("solve").click()


finally:
    time.sleep(10)
    browser.quit()