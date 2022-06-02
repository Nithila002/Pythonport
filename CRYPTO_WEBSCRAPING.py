#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries 

from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


# store website in variable

website = 'https://www.coingecko.com/'


# In[3]:


# get request

response = requests.get(website)


# In[4]:


# status code

response.status_code


# In[5]:


# soup object

soup = BeautifulSoup(response.content, 'html.parser')


# In[6]:


# results

results = soup.find('table',{'class':'table-scrollable'}).find('tbody').find_all('tr')


# In[7]:


# name

results[0].find('a', {'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip()


# In[8]:


# price

results[0].find('span',{'data-target':'price.price'}).get_text()


# In[9]:


# 1hr change

results[0].find('span', {'data-target':'percent-change.percent'}).get_text()


# In[10]:


# 24hr change

results[0].find('td', {'class':'td-change24h'}).get_text().strip()


# In[11]:


# 7d change

results[0].find('td', {'class':'td-change7d'}).get_text().strip()


# In[12]:


#24h volume

results[0].find('td', {'class':'td-liquidity_score'}).get_text().strip()


# In[13]:


#market cap

results[0].find('td', {'class':'td-market_cap'}).get_text().strip()


# In[14]:


# FOR-LOOP

# empty lists

name = []
price = []
change_1h = []
change_24h = []
change_7d = []
volume_24h = []
market_cap = []

for result in results:
       
        
    # name
    try:
        name.append(result.find('a', {'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
    except:
        name.append('n/a')
        
   # price
    try:
        price.append(result.find('span',{'data-target':'price.price'}).get_text())
    except:
        price.append('n/a')
        
   # change_1h
    try:
        change_1h.append(result.find('span', {'data-target':'percent-change.percent'}).get_text())
    except:
        change_1h.append('n/a')
        
    # change_24h
    try:
        change_24h.append(result.find('td', {'class':'td-change24h'}).get_text().strip())
    except:
        change_24h.append('n/a')
        
    # change_7d
    try:
        change_7d.append(result.find('td', {'class':'td-change7d'}).get_text().strip())
    except:
        change_7d.append('n/a')
        
    # volume_24h
    try:
        volume_24h.append(result.find('td', {'class':'td-liquidity_score'}).get_text().strip())
    except:
        volume_24h.append('n/a')
        
            
    # market_cap
    try:
        market_cap.append(result.find('td', {'class':'td-market_cap'}).get_text().strip())
    except:
        market_cap.append('n/a')
    


# In[15]:


# create pandas dataframe

crypto_df = pd.DataFrame({'Coin': name, 'Price':price, 'Change_1h':change_1h, 'Change_24h':change_24h, 'Change_7d':change_7d, 'Volume_24h':volume_24h, 'Market_Cap':market_cap})


# In[16]:


# output dataframe

crypto_df


# In[17]:


# saving in excel

crypto_df.to_excel('single_page_crpto.xlsx', index=False)


# In[18]:


# pagination (get 1000 results)

# empty lists
name = []
price = []
change_1h = []
change_24h = []
change_7d = []
volume_24h = []
market_cap = []

for i in range (1,11):
    
    # website
    website = 'https://www.coingecko.com/en?page=' + str(i)
        
    # request to website
    response = requests.get(website)
    
    # soup obbject
    soup =  BeautifulSoup(response.content, 'html.parser')
    
    # results
    results = soup.find('table',{'class':'table-scrollable'}).find('tbody').find_all('tr')
    
    
for result in results:
       
        
 # name
    try:
        name.append(result.find('a', {'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip())
    except:
        name.append('n/a')
        
 # price
    try:
        price.append(result.find('span',{'data-target':'price.price'}).get_text())
    except:
        price.append('n/a')
        
 # change_1h
    try:
        change_1h.append(result.find('span', {'data-target':'percent-change.percent'}).get_text())
    except:
        change_1h.append('n/a')
        
 # change_24h
    try:
        change_24h.append(result.find('td', {'class':'td-change24h'}).get_text().strip())
    except:
        change_24h.append('n/a')
        
 # change_7d
    try:
        change_7d.append(result.find('td', {'class':'td-change7d'}).get_text().strip())
    except:
        change_7d.append('n/a')
        
 # volume_24h
    try:
        volume_24h.append(result.find('td', {'class':'td-liquidity_score'}).get_text().strip())
    except:
        volume_24h.append('n/a')
        
            
 # market_cap
    try:
        market_cap.append(result.find('td', {'class':'td-market_cap'}).get_text().strip())
    except:
        market_cap.append('n/a')


# In[19]:


# create pandas dataframe

crypto_df = pd.DataFrame({'Coin': name, 'Price':price, 'Change_1h':change_1h, 'Change_24h':change_24h, 'Change_7d':change_7d, 'Volume_24h':volume_24h, 'Market_Cap':market_cap})


# In[20]:


crypto_df


# In[21]:


# saving in excel

crypto_df.to_excel('Full_crpto.xlsx', index=False)


# In[ ]:




