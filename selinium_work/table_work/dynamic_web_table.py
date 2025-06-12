'''
Created on 31 May 2025

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

'''Dynamic table'''
row_list = driver.find_elements(By.XPATH, '//*[@id="rows"]/tr')
rows_count = len(row_list)

expected_name = input("name")
for j in range (2, rows_count+1):
    name_cell = driver.find_element(By.XPATH, f'//*[@id="rows"]/tr[j]/td')
    actual_name = name_cell.text
    if expected_name == actual_name:
        memory_cell = driver.find_element(By.XPATH, f"//*[id='rows']/tr[{j}]//td[contains(text(),'MB')and not(contains(text(), '/s'))]")
        memory= memory_cell.text
        print(memory)
        break
    else:
        print("book not found")
    
    
    

#//*[@id="rows"]/tr[1]/td[2]
#//td[contains(text(),'MB') and not(contains(text(), '/s' ))]
#//td[contains(text(), 'MB' and not (contains(text(),'/s')]
