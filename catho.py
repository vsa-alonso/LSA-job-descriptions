# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 17:55:46 2019

@author: valonso.iphac
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome(executable_path=r'C:\Users\vsaal\Downloads\chromedriver_win32\chromedriver.exe')

driver.get('https://www.catho.com.br/vagas/data-scientist/')
soup = BeautifulSoup(driver.page_source, 'lxml')

i=0
while i<11:
    time.sleep(5)
    i = i+1
    continuar_lendo = "/html/body/div[1]/div[3]/main/div[3]/div/div/section/ul/li[" + str(i) + "]/article/div/div[1]/button"
    driver.find_element_by_xpath(continuar_lendo).click()
    print("Abrimos a descricao numero {}".format(i))



driver.find_element_by_xpath("/html/body/div[1]/div[3]/main/div[3]/div/div/section/ul/li[i]/article/div/div[1]/button").click()
continuar_lendo = "/html/body/div[1]/div[3]/main/div[3]/div/div/section/ul/li[" + str(i) + "]/article/div/div[1]/button"
driver.find_element_by_xpath(continuar_lendo).click()






descricao = []

# Grab the information I need and append it in a list called descricao

driver.find_element_by_xpath("/html/body/div[1]/div[3]/main/div[3]/div/div/section/ul/li[1]/article/div/div[1]/button").click()
driver.find_element_by_xpath('/html/body/div[1]/div[3]/main/div[3]/div/div/section/ul/li[2]/article/div/div[1]/button').click()
driver.find_element_by_xpath('/html/body/div[1]/div[3]/main/div[3]/div/div/section/ul/li[3]/article/div/div[1]/button').click()
driver.find_element_by_xpath('/html/body/div[1]/div[3]/main/div[3]/div/div/section/ul/li[5]/article/div/div[1]/button').click()
driver.find_element_by_id("span", 'button aria-label').click()
soup = BeautifulSoup(driver.page_source, 'lxml')

price = [a.get("aria-label") for a in soup.findAll('button', {"class":'sc-Rmtcm tNXgw button-expanded'})]

i=0




content = soup.findAll('button', {"class":'sc-Rmtcm tNXgw button-expanded'})["aria-label"][1]
soup.find('div', 'sc-csuQGl bpzOnV').get_text()

 


content = [texto for texto in soup.findAll('button', {"class":'sc-Rmtcm tNXgw button-expanded'})["aria-label"]]




driver.find_element_by_class_name('abrir vaga').click()
driver.find_elements_by_link_text('continuar lendo').click()

for i in range(2,16):
    while True:
        try:
            driver.find_element_by_class_name('abrir vaga').click()
            time.sleep(1)
        except:
            print('Terminou a pagina' + str(i))
            break
    
    
    lista = [texto.text for texto in driver.find_elements_by_class_name('job-description')]
    descricao.append(lista)
    driver.find_element_by_link_text(str(i)).click()
    time.sleep(2)

kk=[item for sublist in descricao for item in sublist]
driver.close()

with open('catho.txt', 'w') as f:
    for item in kk:
        f.write("%s\n\n" % item)
