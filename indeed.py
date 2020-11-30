# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:55:46 2019

@author: valonso.iphac
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random

driver = webdriver.Chrome(executable_path=r'C:\Users\vsaal\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://www.indeed.com/q-Data-Scientist-jobs.html')
soup = BeautifulSoup(driver.page_source, 'lxml')

#soup.findAll('div', 'jobsearch-jobDescriptionText')

descricao = []
page=1


# Fucntion designed to get the informations needed
def Get_descriptions():
    for link in driver.find_elements_by_class_name('title'):
        # I open the link in the website to the jog description
        link.click()
        time.sleep(random.randrange(2,4))
        # Make Selenium realize it has to go wor in that tab
        driver.switch_to_window(driver.window_handles[1])
        # Get the Beautiful Soup outta that page
        soup = BeautifulSoup(driver.page_source, 'lxml')
        # Grab the information I need and append it in a list called descricao
        content = soup.find('div', 'jobsearch-jobDescriptionText').get_text().strip()
        descricao.append(content)
        # Close that tab and go another round
        driver.close()
        driver.switch_to_window(driver.window_handles[0])


        
# Sometimes a pop up page appears, this brings great trouble to selenium. Thus this function will find if the pop up is there
def did_pop_up_page_appear():
    try:
        driver.find_element_by_link_text('No, thanks')
    except:
        return False
    return True



# Main function
while driver.find_element_by_link_text('Next »'):
    try:
        Get_descriptions()
        driver.find_element_by_link_text('Next »').click()
        time.sleep(5)
        if did_pop_up_page_appear():
            driver.find_element_by_link_text('No, thanks').click()
        else:
            continue
    except:
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        continue
    
    
    
with open('catho_completo.txt', 'w', encoding="utf-8") as f:
    for item in descricao:
        f.write("%s\n\n****_*\n\n" % item)





