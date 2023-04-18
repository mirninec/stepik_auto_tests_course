from selenium import webdriver
from selenium.webdriver.common.by import By
import math 
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, '//*[@id="input_value"]')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
    input1.send_keys(y)
    checkbox = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]').click()
    radioButton = browser.find_element(By.XPATH, '//*[@id="robotsRule"]').click()
    time.sleep(1)
    submitButton = browser.find_element(By.XPATH, "/html/body/div[1]/form/button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла