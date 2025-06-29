from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pyperclip
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    price = WebDriverWait(browser,13).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()


    input_value_css= browser.find_element(By.ID, "input_value")
    x=int(input_value_css.text)
    value=calc(x)

    answer_css= browser.find_element(By.ID,"answer")
    answer_css.send_keys(value)

    button1 = browser.find_element(By.ID, "solve")
    button1.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    #копирование с алерта в снтр+с
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
