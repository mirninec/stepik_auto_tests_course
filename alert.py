from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math 

link = "https://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    alert_button = browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    browser.switch_to.alert.accept()

    x_element = browser.find_element(By.ID, 'input_value')
    x = int(x_element.text)
    result = calc(x)

    input_element = browser.find_element(By.ID, 'answer')
    input_element.send_keys(str(result))

    submit_element = browser.find_element(By.XPATH, '//button[@type="submit"]').click()

    print(browser.switch_to.alert.text)
    browser.switch_to.alert.accept()

finally:
    # успеваем скопировать код за 30 секунд
    # time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла