from selenium import webdriver
import math

link = "http://SunInJuly.github.io/execute_script.html"
b = webdriver.Chrome()
b.get(link)

x = b.find_element_by_css_selector("#input_value").text
ex = str(math.log(abs(12*math.sin(int(x)))))
answer = b.find_element_by_css_selector("#answer").send_keys(ex)
b.execute_script("window.scrollBy(0, 100);")
b.find_element_by_css_selector("#robotCheckbox").click()
b.find_element_by_css_selector("#robotsRule").click()
b.find_element_by_css_selector(".btn").click()