from selenium import webdriver
from selenium.webdriver.common.by import By
import math 
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.ID, 'input_value').text
    # num1 = int(num1_element.text)  
    result = calc(num1_element)
    input1 = browser.find_element(By.ID, 'answer').send_keys(result)
    browser.execute_script("window.scrollBy(0, 100);")
    checkbox = browser.find_element(By.ID, 'robotCheckbox').click()
    radio = browser.find_element(By.ID, 'robotsRule').click()
    submitButton = browser.find_element(By.TAG_NAME, "button")
    submitButton.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла