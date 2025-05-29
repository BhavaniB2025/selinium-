'''
Created on 24 May 2025

@author: Bhavani
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options)
driver.implicitly_wait(10)

'''navigate to iframe with in an iframe'''
driver.get('https://demo.automationtesting.in/Frames.html')

'''switch to iframe '''
iframe_with_in_an_iframe = driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]')
iframe_with_in_an_iframe.click()


'''switch to outer frame (nested frame)'''
nested_frame = driver.find_element(By.XPATH, '//*[@id="Multiple"]/iframe')
driver.switch_to.frame(nested_frame)

'''switch to inner frame (iframe demo ) '''
inner_frame = driver.find_element(By.XPATH, '/html/body/section/div/div/iframe')
driver.switch_to.frame(inner_frame)

'''enter text in text box'''
input_txt_bx = driver.find_element(By.XPATH, '/html/body/section/div/div/div/input')
input_txt_bx.send_keys("bhavani")


'''
driver.switch_to.frame(13)
singleframe_txt_bx = driver.find_element(By.XATH, '/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[1]/a')
singleframe_txt_bx.click()


form_txt_bx = driver.find_element(By.XPATH, '/html/body/section/div/div/div/input')
form_txt_bx.send_keys("Bhavani")

nested_iframe_txt_bx = driver.find_element(By.XATH, '/html/body/section/div/div/h5')
nested_iframe_txt_bx.click()


iframe_txt_bx = driver.find_element(By.XATH, '/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a')
iframe_txt_bx.click()
'''
