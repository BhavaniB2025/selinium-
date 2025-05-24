'''
Created on 19 May 2025

@author: Bhavani
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from idlelib.idle_test.test_textview import ButtonClickTest
from email._header_value_parser import Address

'1. launching the chrome browser'
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)


driver.get('https://selenium.dev/')

'Navigate to practice site'
driver.get('https://testautomationpractice.blogspot.com/?m=1')

'Enter name'
name_txt_bx = driver.find_element(By.ID, 'name')
name_txt_bx.send_keys("Bhavani")

email_txt_bx = driver.find_element(By.ID, 'email' )
email_txt_bx.send_keys("bhavani.bakale@gmail.com")

phonenumber_txt_bx = driver.find_element(By.ID, 'phone' )
phonenumber_txt_bx.send_keys("7996096944")

address_txt_bx = driver.find_element(By.ID, 'textarea' )
address_txt_bx.send_keys("holenarasipura")

female_txt_bx = driver.find_element(By.ID, 'female')
female_txt_bx.click()

saturday_txt_bx = driver.find_element(By.ID ,'saturday')
saturday_txt_bx.click()

monday_txt_bx = driver.find_element(By.ID ,'monday')
monday_txt_bx.click()

tuesday_txt_bx = driver.find_element(By.ID ,'tuesday')
tuesday_txt_bx.click()

wednesday_txt_bx = driver.find_element(By.ID ,'wednesday')
wednesday_txt_bx.click()

thursday_txt_bx = driver.find_element(By.ID ,'thursday')
thursday_txt_bx.click()

friday_txt_bx = driver.find_element(By.ID ,'friday')
friday_txt_bx.click()

country_txt_bx = driver.find_element(By.ID ,'country')
country_txt_bx.send_keys("country")

start_txt_bx = driver.find_element(By.XPATH, '//*[@id="HTML5"]/div[1]/button')
start_txt_bx.click()

simple_alert_txt_bx = driver.find_element(By.ID ,'alertBtn')
simple_alert_txt_bx.click()

'''
confirmation_alert_txt_bx = driver.find_element(By.ID, 'confirmBtn')
confirmation_alert_txt_bx.click()

prompt_alert_txt_bx = driver.find_element(By.ID, 'prompBtn')
prompt_alert_txt_bx.click()
'''
wiki_search_input = driver.find_element(By.ID, 'wikipedial_wikipedia = search.input')
wiki_search_input.send_key("selenium")
'''
wiki_search_btn = driver.find(By.XPATH, ' //*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input'')
wiki_search_buttonclick()

time.sleep(60)
history_link = driver.find_element(By.XPATH, '//*[@id="toc-History"]/a/div/span[2]' )
history_link.click()
'''



