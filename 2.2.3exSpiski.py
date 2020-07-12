from selenium import webdriver
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = int(x_element.text)
    y_element = browser.find_element_by_id("num2")
    y = int(y_element.text)
    res = str(x + y)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(res)

    button = browser.find_element_by_tag_name('[type="submit"]').click()

finally:
    browser.quit()