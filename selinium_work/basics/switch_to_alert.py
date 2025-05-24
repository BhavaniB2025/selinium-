'''
Created on 23 May 2025

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

'''3.simple alert'''
simple_alert_btn = driver.find_element(By.ID, 'alertBtn')
simple_alert_btn.click()

simple_alert = driver.switch_to.alert

simple_alert_text = simple_alert.text
print(simple_alert.text)
time.sleep(3)
simple_alert.accept()

confirmation_alert_btn = driver.find_element(By.ID, 'confirmBtn')
confirmation_alert_btn.click()
confirmation_alert = driver.switch_to.alert
confirmation_alert_text = confirmation_alert.text

prompt_alert_btn = driver.find_element(By.ID, 'promptBtn')
prompt_alert_btn.click()
prompt_alert = driver.switch_to.alert
prompt_alert_text = prompt_alert.text
