link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert button.is_displayed() == True, "кнопка не отображается"
