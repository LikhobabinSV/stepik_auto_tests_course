import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

from conftest import browser


@pytest.fixture(scope="session")
def auth_fixture(browser):
    browser.get("https://stepik.org/login")
    login = ''
    password = ''

    text_box_email = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    text_box_email.send_keys(login)

    text_box_pass = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    text_box_pass.send_keys(password)

    button_login = browser.find_element(By.CLASS_NAME, "button_with-loader")
    button_login.click()
    time.sleep(2)
    return browser

@pytest.mark.parametrize("link", [
"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_text_link(auth_fixture, link):
    browser= auth_fixture
    browser.get(link)

    text_area = browser.find_element(By.CLASS_NAME, "ember-text-area")
    answer = math.log(int(time.time()))
    text_area.send_keys(answer)

    button = browser.find_element(By.CLASS_NAME,"submit-submission")
    button.click()

    time.sleep(4)
    text_area1 = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
    assert text_area1.text=="Correct!", f"Ошибка в {link} текст{text_area1.text}"


