import requests
from bs4 import BeautifulSoup
import pandas as pd
headLine_list =[]
url = 'https://www.ndtv.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

head_lines = soup.find_all('h3')
#print(soup.prettify())

for i in head_lines:
    headLine_list.append(i.text)

#print(headLine_list)

with open("headline.text", "w", encoding="utf-8") as file:
    for i, line in enumerate(headLine_list, start=0):   
        file.write(f"{i+1}. {line}\n")
    