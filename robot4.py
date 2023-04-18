from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math 
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.XPATH, '//*[@id="num1"]')
    num1 = int(num1_element.text)  
    num2_element = browser.find_element(By.XPATH, '//*[@id="num2"]')
    num2 = int(num2_element.text)
    sumNums = num1 + num2
    print(sumNums)
    select = Select(browser.find_element(By.XPATH, '//*[@id="dropdown"]'))
    select.select_by_value(str(sumNums))
    submitButton = browser.find_element(By.XPATH, "/html/body/div[1]/form/button").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла