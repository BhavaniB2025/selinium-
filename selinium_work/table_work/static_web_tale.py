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

row_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody')
rows_count = len(row_list)

print("rows_count", rows_count)
for j in range(2,8):
    for i in range (1,5):
        table_cell = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody')
        print(table_cell)
    
    
'''
cell_22 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[2]')
cell_22_text = cell_22.text
print(cell_22_text)

cell_23 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]')
cell_23_text = cell_23.text
print(cell_23_text)

cell_31 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[1]')
cell_31_text = cell_31.text
print(cell_31_text)

cell_32 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[2]')
cell_32_text = cell_32.text
print(cell_32_text)

cell_33 = driver.find_element(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[3]')
cell_33_text = cell_33.text
print(cell_33_text)
'''


'''
//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[2]
//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[3]
//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td[4]

//*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[1]
'''