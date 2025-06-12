'''
Created on 2 Jun 2025

@author: Bhavani
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''1. Launching the chrome browser'''
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
# driver = Chrome()
driver.implicitly_wait(10)

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''locate shodow host'''
shadow_host = driver.find_element(By.ID, 'shadow_host')

'''get shadow root present in shadow host'''
my_shadow_root = shadow_host.shadow_root

'''find the element inside the root'''
shadow_input_text_field = my_shadow_root.find_element(By.CSS_SELECTOR, 'input[type=text]:nth-child(5)')   #copy selector for this
shadow_input_text_field.send_keys("Bhavani")