from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CLASS_NAME, 'second')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'third')
    input3.send_keys("my@email.ru")
    input4 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[1]/input")
    input4.send_keys("27317")
    input5 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[2]/div[2]/input")
    input5.send_keys("cat")
    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла