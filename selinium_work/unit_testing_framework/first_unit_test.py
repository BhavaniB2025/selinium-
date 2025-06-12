'''
Created on 11 Jun 2025

@author: KATWA
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pip._vendor.typing_extensions import Self

class OrangeHRMLoginTest(unittest.TestCase):


    def test_navigation_to_login_page(self):
        '1. launching the chrome browser'
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options)
        
        'Navigate to OrangeHRM login page '
        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        
        '''Validate whether navigation is successful'''
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        expected_url_position = "auth/login"
        actual_url= driver.current_url
        #self.assertEqual(actual_url, expected_url, "Navigation to OrangeHRM login page is failed ")
        self.assertIn(expected_url_position, actual_url,  "Navigation to OrangeHRM login page is failed ")
        
    def Test_orangeHRM_loginTest(self):
        
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options)
        
        '''Enter user name'''
        username_bx = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
        username_bx.send_keys("admin123")
    
        
        '''Enter password'''
        password_bx = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
        password_bx.send_keys("Admin")
        
        '''login '''
        
        login_btn = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
        login_btn.click()
        
        '''Validate whether navigate is successful'''
        expected_url_memeber = "dashboard/index"
        actual_url = driver.current_url
        
        self.assertIn( expected_url_memeber, actual_url, "login failed")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()