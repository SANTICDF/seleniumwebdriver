from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get("www.facebook.com")
element = driver.find_element(By.ID, "email")
element.clear()
element.send_keys("Test@gmail.com")
element_pass = driver.find_element(By.ID, "pass")
element_pass.clear()
element_pass.send_keys("Password")

login_button_element = driver.find_element(By.NAME, "login")
login_button_element.click()
time.sleep(113000)
