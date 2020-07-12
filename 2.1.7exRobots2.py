from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    check = browser.find_element_by_id("robotCheckbox").click()

    radio = browser.find_element_by_tag_name('[for="robotsRule"]').click()

    button = browser.find_element_by_tag_name('[type="submit"]').click()


finally:
    browser.quit()