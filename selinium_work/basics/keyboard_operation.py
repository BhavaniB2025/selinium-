'''
Created on 26 May 2025

@author: Bhavani
'''
from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)

driver.implicitly_wait(10)

'''2. Navigating to practice site'''
driver.get('https://testautomationpractice.blogspot.com/')

'''creating an object from actionchain class'''
actions_key = ActionChains(driver)

'''coping text from field1 'ctrl+a' '''
field1_txt_bx = driver.find_element(By.ID, 'field1')
actions_key.down(Keys.CONTROL, field1_txt_bx).send_keys('a').key_up(Keys.CONTROL).perform()

'''Pasting the text in field 2'''

