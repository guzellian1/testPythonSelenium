from selenium import webdriver
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector("input:required.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("input:required.form-control.second")
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector("input:required.form-control.third")
        input3.send_keys("gggg@gmail.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(2)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()

    def test_reg2(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector("input:required.form-control.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("input:required.form-control.second")
        input2.send_keys("Ivanov")
        input3 = browser.find_element_by_css_selector("input:required.form-control.third")
        input3.send_keys("gggg@gmail.com")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(2)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()

if __name__ == "__main__":
    unittest.main()