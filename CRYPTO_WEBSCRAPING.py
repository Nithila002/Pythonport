CRYPTO CURRENCY WEB SCRAPING

Single_Page
# import libraries 

from bs4 import BeautifulSoup
import requests
import pandas as pd

# store website in variable

website = 'https://www.coingecko.com/'

# get request

response = requests.get(website)

# status code

response.status_code

# soup object

soup = BeautifulSoup(response.content, 'html.parser')

# results

results = soup.find('table',{'class':'table-scrollable'}).find('tbody').find_all('tr')

# name

results[0].find('a', {'class':'tw-hidden lg:tw-flex font-bold tw-items-center tw-justify-between'}).get_text().strip()

# price

results[0].find('span',{'data-target':'price.price'}).get_text()

# 1hr change

results[0].find('span', {'data-target':'percent-change.percent'}).get_text()

# 24hr change

results[0].find('td', {'class':'td-change24h'}).get_text().strip()

# 7d change

results[0].find('td', {'class':'td-change7d'}).get_text().strip()

#24h volume

results[0].find('td', {'class':'td-liquidity_score'}).get_text().strip()

#market cap

results[0].find('td', {'class':'td-market_cap'}).get_text().strip()

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
    
# create pandas dataframe

crypto_df = pd.DataFrame({'Coin': name, 'Price':price, 'Change_1h':change_1h, 'Change_24h':change_24h, 'Change_7d':change_7d, 'Volume_24h':volume_24h, 'Market_Cap':market_cap})

# output dataframe

crypto_df

# saving in excel

crypto_df.to_excel('single_page_crpto.xlsx', index=False)

Multi_Page
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


# create pandas dataframe

crypto_df = pd.DataFrame({'Coin': name, 'Price':price, 'Change_1h':change_1h, 'Change_24h':change_24h, 'Change_7d':change_7d, 'Volume_24h':volume_24h, 'Market_Cap':market_cap})

# saving in excel

crypto_df.to_excel('Full_crpto.xlsx', index=False)





