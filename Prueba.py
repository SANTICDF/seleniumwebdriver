# Elian Rosales

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome()

# Guardamos la URL del formulario en una variable para poder acceder a ella más fácilmente 
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLScz2mqlmoHNqlXgEdd_Q4blqBSA73-Z7HMQpDhQDo1KmSJrNg/viewform'
driver.get(form_url)

#Nombre
name_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
name_field.send_keys('Elián')

# Apelido
last_name_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
last_name_field.send_keys('Rosales')

# Edad
age_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
age_field.send_keys('20')

# Correo
email_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
email_field.send_keys('elianrosales854@gmail.com')

# Fecha
date_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
date_field.send_keys('06/06/2024')

# Enviar
submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit_button.click()

time.sleep(3)

driver.quit()
