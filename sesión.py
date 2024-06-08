from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()
driver.get("https://mail.google.com")

time.sleep(2)

email_field = driver.find_element(By.ID, "identifierId")
email_field.clear()
email_field.send_keys("tu_correo@gmail.com")
next_button = driver.find_element(By.ID, "identifierNext")
next_button.click()
time.sleep(2)
password_field = driver.find_element(By.NAME, "password")
password_field.clear()
password_field.send_keys("tu_contraseña")
password_next_button = driver.find_element(By.ID, "passwordNext")
password_next_button.click()
time.sleep(5)
driver.quit()
