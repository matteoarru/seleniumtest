#!../venv python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:03:35 2020

@author: matteoarru
"""

import time
from selenium import webdriver

driver = webdriver.Chrome('./resources/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()
