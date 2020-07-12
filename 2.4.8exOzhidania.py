from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  browser.implicitly_wait(5)
  link = "http://suninjuly.github.io/explicit_wait2.html"
  browser.get(link)

  button = WebDriverWait(browser, 12).until(
      EC.text_to_be_present_in_element((By.ID, "price"), "$100")
  )

  book = browser.find_element_by_id('book').click()

  x_element = browser.find_element_by_id("input_value")
  x = x_element.text
  y = calc(x)

  input = browser.find_element_by_id("answer")
  input.send_keys(y)

  submit = browser.find_element_by_tag_name('[type="submit"]').click()

finally:
  browser.quit()