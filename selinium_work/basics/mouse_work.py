'''
Created on 25 May 2025

@author: bhavani
'''

from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)

'''creating an object from actionchain class'''
actions = ActionChains(driver)

'''2. Navigating to practice site'''
driver.get('https://demo.guru99.com/test/simple_context_menu.html')
right_click_me_btn = driver.find_element(By.XPATH, '//*[@id="authentication"]/span')
actions.context_click(right_click_me_btn).perform()
