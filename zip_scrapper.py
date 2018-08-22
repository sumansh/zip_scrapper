# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 18:02:47 2018

@author: Sumansh
"""

import os

path = r'C:\Users\Sumansh\Downloads\data_2017'

os.chdir(path)


headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}

import pandas as pd


zip_codes = pd.read_excel("./data.xlsx")


import requests
from bs4 import BeautifulSoup



a  = list(zip_codes.result_zip_code)

final = pd.DataFrame()
for i in a:
    link  = 'https://www.unitedstateszipcodes.org/' + str(i) + '/'
    
    page = requests.get(link,headers=headers)
    page.status_code
    
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.find_all('div', class_='col-xs-12 col-sm-6')
    data1 = data[0]
    data2 = data[1]
    
    
    
    
    table = data1.find('tbody')
    
    list_of_rows = []
    for row in table.findAll('tr'):
        list_of_cells = []
        for cell in row.findAll('th'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)
    
    
    table = data2.find('tbody')
    
    for row in table.findAll('tr'):
        list_of_cells = []
        for cell in row.findAll('th'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        for cell in row.findAll('td'):
            text = cell.text.replace('&nbsp;', '')
            list_of_cells.append(text)
        list_of_rows.append(list_of_cells)   
    
    ff  = pd.DataFrame(list_of_rows)
    ff = ff.T
    ff.columns = ff.iloc[0]
    ff = ff.iloc[1:2,:]
    ff['Zip Code'] = str(i)
    final = final.append(ff)


final.to_csv('out.csv', index =False)
