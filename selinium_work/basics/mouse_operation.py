'''
Created on 25 May 2025

@author: bhavani
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
actions = ActionChains(driver)

'''scrolling'''
#actions.scroll_by_amount(0, 1000).perform()

'''mouse hover'''
'''point_me = driver.find_element(By.XPATH ,'//*[@id="HTML3"]/div[1]/div/button')
actions.move_to_element(point_me).perform()

'''double click'''
copy_text_btn =  driver.find_element(By.XPATH ,'//*[@id="HTML10"]/div[1]/button')
actions.double_click(copy_text_btn).perform

'''Drag and drop'''
actions.scroll_by_amount(0, 500).perform()
source = driver.find_element(By.ID, 'draggable')
target = driver.find_element(By.ID, 'droppable')
actions.drag_and_drop(source, target).perform()

'''slidder'''

slidder_right_box = driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[2]')
actions.drag_and_drop_by_offset(slidder_right_box, 50, 0).perform()

slidder_left_box = driver.find_element(By.XPATH, '//*[@id="slider-range"]/span[1]')
actions.drag_and_drop_by_offset(slidder_left_box, 15, 0).perform()
'''
driver.get('https://demo.guru99.com/test/simple_context_menu.htmll')
right_click_me_btn = driver.find_element(By.XPATH, '//*[@id="authentication"]/span")
actions.context_click(right_click_me_btn).perform()

'''
'''coping text from field1 'ctrl+a' '''
field1_txt_bx = driver.find_element(By.ID, 'field1')
actions.key_down(Keys.CONTROL, field1_txt_bx).send_keys('a').key_up(Keys.CONTROL).perform()

'''Pasting the text in field 2   'ctrl+c'  '''
field1_txt_bx = driver.find_element(By.ID, 'field1')
actions.key_down(Keys.CONTROL, field1_txt_bx).send_keys('v').key_up(Keys.CONTROL).perform()


'''Pasting text to field2   'ctrl+v' '''
field2_txt_bx = driver.find_element(By.ID, 'field2')
actions.key_down(Keys.CONTROL, field2_txt_bx).send_keys('a').key_up(Keys.CONTROL).perform()











