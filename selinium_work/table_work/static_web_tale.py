'''
Created on 29 May 2025

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


'''print value from each cell'''
cell_21 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[1]' )
cell_21_text = cell_21.text
print(cell_21_text)
                            