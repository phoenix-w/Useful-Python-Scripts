# scrape wikipedia table and save as dataframe

import pandas as pd
import requests 
from bs4 import BeautifulSoup 

wikiurl = "LINK-TO-WIKI-TABLE"
response = requests.get(wikiurl)
print(response.status_code) # 200 means everything's ready to go

soup = BeautifulSoup(response.text, 'html.parser')
indiatable = soup.find('table', {'class':"wikitable"})
df = pd.read_html(str(indiatable))
df = pd.DataFrame(df[0])

# table is now converted into a dataframe
print(df.head())