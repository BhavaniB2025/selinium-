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

row_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr')
rows_count = len(row_list)

'''
expected_book =input("Enter book name")
'''
column_list = driver.find_elements(By.XPATH, '//*[@id="HTML1"]/div[1]/table/tbody/tr[2]/td')
column_count = len(column_list)
'''
for j in range(2, rows_count+1):
    for i in range (1,column_count+1):
        table_cell = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody')
        table_cell_value = table_cell.text
        
        print(table_cell_value)
        
'If the entity column name is same then print its price'
Learn_Java  = driver.find_element(By.XPATH ,'//*[@id="HTML1"]/div[1]/table/tbody/tr[3]/td[1]')
Learn_Java_value = Learn_Java.text
print(Learn_Java_value)

'''

'''Assignment question for to print price of book '''
name = input("enter book name")
for j in range (2, rows_count+1):
    book_name = driver.find_element(By.XPATH, f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{j}]/td[1]')
    book_name = book_name.text
    print(book_name)
    price = driver.find_element(By.XPATH , f'//*[@id="HTML1"]/div[1]/table/tbody/tr[{j}]/td[4]')
    price = price.text 
    if book_name == name:
        print("price of ",book_name,"is", price)
        break
else:
    print("Book not found")  
        
        