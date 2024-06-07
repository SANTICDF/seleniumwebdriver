# Elian Rosales

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome()

# Guardamos la URL del formulario en una variable para poder acceder a ella más fácilmente 
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdRO5HUdmu167N7cRqJV0X90qrI5yyUQSTwv6ma9xZiHbdHKw/viewform?usp=sf_link'
driver.get(form_url)

wait = WebDriverWait(driver, 20)

# Nombre
name_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
name_field.clear()
name_field.send_keys('Elian')

# Apellido
last_name_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
last_name_field.clear()
last_name_field.send_keys('Rosales')

# Edad
age_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
age_field.clear()
age_field.send_keys('20')

# Correo
email_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')))
email_field.clear()
email_field.send_keys('elianrosales854@gmail.com')

# Fecha
date_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')))
date_field.clear()
date_field.send_keys('06/06/2024')

# Enviar
submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
submit_button.click()

time.sleep(3)

driver.quit()
