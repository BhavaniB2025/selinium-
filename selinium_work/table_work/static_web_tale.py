'''
Created on 29 May 2025

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

'''3. Print value from each cell'''

cell_21 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[1]')
cell_21_text = cell_21.text
print(cell_21_text)

cell_22 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[2]')
cell_22_text = cell_22.text
print(cell_22_text)

'''
//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[2]
//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]
//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[4]

//*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[1]
'''