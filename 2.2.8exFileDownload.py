from selenium import webdriver
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element_by_tag_name('[name="firstname"]')
    input1.send_keys("Guzel")

    input2 = browser.find_element_by_tag_name('[name="lastname"]')
    input2.send_keys("Sabirova")

    input3 = browser.find_elements_by_tag_name('[name="email"]')
    input3.send_keys("guzel@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__)) #получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt') #добавляем к этому пути имя файла

    file = browser.find_element_by_id("file")
    file.send_keys(file_path)

finally:
    browser.quit()
