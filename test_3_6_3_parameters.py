import pytest
import time
import math
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('lesson', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_find_hidden_text(browser, lesson):
    link = f'https://stepik.org/lesson/{lesson}/step/1'
    browser.implicitly_wait(6)
    browser.get(link)
    answer = math.log(int(time.time()))
    input = browser.find_element_by_css_selector(".textarea")
    input.send_keys(str(answer))
    browser.find_element_by_css_selector(".submit-submission").click()
    nadpis = browser.find_element_by_css_selector(".smart-hints__hint")
    assert nadpis.text == "Correct!", "Uncorrect value"