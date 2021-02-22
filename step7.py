from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_class_name("first")
    name.send_keys("Arina")
    last_name = browser.find_element_by_css_selector("[placeholder='Input your last name']")
    last_name.send_keys("Kamliuk")
    email = browser.find_element_by_class_name("third")
    email.send_keys("kgktfk")


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()