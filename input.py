from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os 

link = "https://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, '//input[@placeholder="Enter first name"]')
    input1.send_keys('cat')
    input2 = browser.find_element(By.XPATH, '//input[@placeholder="Enter last name"]')
    input2.send_keys('cat')
    input3 = browser.find_element(By.XPATH, '//input[@placeholder="Enter email"]')
    input3.send_keys('cat@cat.com')
    file = browser.find_element(By.XPATH, "//input[@type='file']")
    file.send_keys(file_path)
    
    submitButton = browser.find_element(By.TAG_NAME, "button")
    submitButton.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла