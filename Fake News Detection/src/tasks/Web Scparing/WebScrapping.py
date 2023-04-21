# Importing Dependencies
from bs4 import BeautifulSoup
import pandas as pd
import requests 
import urllib.request
import time

headlines = [] # Stored title of the news 
targets = [] # True/False
for pagenumber in range(1,101): # Web Scraping first 100 pages
  pagenumber = str(pagenumber)
  URL = "https://www.politifact.com/factchecks/list/?page"+pagenumber
  webpage = requests.get(URL)
  soup = BeautifulSoup(webpage.text, "html.parser")
  # Fetching title/headline of news
  text = soup.find_all('div',attrs={'class':'m-statement__quote'})
  for i in text:
    link1 = i.find_all('a')
    headline = link1[0].text.strip()
    headlines.append(headline)

  #  Fetching the target which is weather news is true/false
  target = soup.find_all('div',attrs={'class':'m-statement__meter'})
  for j in target:
    link2 = j.find('div',attrs={'class':'c-image'}).find('img').get('alt')
    targets.append(link2)

final_headline = []
final_targets = []
for i in range(len(headlines)):
  if(targets[i] == "pants-fire"):
    final_targets.append("false")
    final_headline.append(headlines[i])
  if(targets[i]=="false" or targets[i]=="true"):
    final_targets.append(targets[i])
    final_headline.append(headlines[i])

# Making DataFrame
data = {'Headline':final_headline,
        'Target':final_targets}
df = pd.DataFrame(data)
# Saving csv file
df.to_csv("/content/PolitiFact01.csv")
