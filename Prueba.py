#Elián Rosales
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://automationintesting.com/selenium/testpage/")


name_field = driver.find_element(By.NAME, "firstname")
name_field.send_keys("John")

name_field = driver.find_element(By.NAME, "surname")
name_field.send_keys("Doe")

dropdown_element = driver.find_element_by_id("gender")
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text("Male")

radio_button = driver.find_element_by_id("red")
if not radio_button.is_selected():
    radio_button.click()

text_area = driver.find_element_by_css_selector("textarea[placeholder='Tell us some fun stuff!']")
text_area.send_keys("Ejemplo Texto")


submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_button.click()

driver.quit()
----------------------
