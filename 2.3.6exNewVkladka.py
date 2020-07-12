from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  link = "http://suninjuly.github.io/redirect_accept.html"
  browser.get(link)

  button = browser.find_element_by_tag_name('[type="submit"]').click()

  new_window = browser.window_handles[1]
  browser.switch_to.window(new_window)

  x_element = browser.find_element_by_id("input_value")
  x = x_element.text
  y = calc(x)

  input = browser.find_element_by_id("answer")
  input.send_keys(y)

  submit = browser.find_element_by_tag_name('[type="submit"]').click()

finally:
  browser.quit()