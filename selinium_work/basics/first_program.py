'''
Created on 11 May 2025

@author: Bhavani
'''

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://selenium.dev/')


from selenium.webdriver import Chrome
driver = Chrome()
driver.get('http://selenium.dev/')

from selenium import webdriver

'1. launching the chrome browser'
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)


driver.get('https://selenium.dev/')

'Navigate to practice site'
driver.get('https://testautomationpractice.blogspot.com/?m=1')

'validate the navigation is successful'
current_page_title=driver.title
print(current_page_title)

expected_page_title= "Automation test practice" 

if current_page_title == expected_page_title:
    print("Test is passed!")
else:
    print("Test is failed!")
    














