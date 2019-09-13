# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 06:21:38 2019

@author: Mengyu Liu
"""
from selenium import webdriver
import time

home='https://scholar.google.com/citations?user=NDrCCokAAAAJ&hl=en#d=gs_md_cita-d&u=%2Fcitations%3Fview_op%3Dview_citation%26hl%3Den%26user%3DNDrCCokAAAAJ%26citation_for_view%3DNDrCCokAAAAJ%3Au5HHmVD_uO8C%26tzom%3D300'
driver=webdriver.Firefox()
driver.get(home)
driver.implicitly_wait(10)
title_path = "//a[@class='gsc_vcd_title_link']"
title =  driver.find_element_by_xpath(title_path).get_attribute('textContent')
print(title)
author_path = "//div[@class='gsc_vcd_value']"
author = driver.find_element_by_xpath(author_path).get_attribute('textContent')
print(author)
abstract_path = "//div[@class='gsh_csp']"
abstrct = driver.find_element_by_xpath(abstract_path).get_attribute('textContent')
print(abstrct)
