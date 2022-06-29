import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import pandas as pd



page=urllib.request.Request('https://cod.tracker.gg/cold-war/leaderboards/stats/psn/Kills?page=1',headers={'User-Agent': 'Mozilla/5.0'})
infile=urllib.request.urlopen(page).read()
data = infile.decode('ISO-8859-1')



page_soup = soup(data,"html.parser")

container = page_soup.findAll("div",{"class":"board"})

table = container[0].table


user = table.tbody.findAll("span",{"class":"trn-ign__username"})
kc = table.tbody.findAll("td",{"class":"stat"})



filename = "kd.csv"
x = {"username":[], "kills":[], "games":[]}

for i in range(0,len(user)):
    x['username'].append(user[i].text)

for i in range(0,(len(user))*2,2):
    x['kills'].append(kc[i].text.strip().replace(',', ''))
    x['games'].append(kc[i+1].text.strip().replace(',', ''))

df = pd.DataFrame(x)
df.to_csv(filename, index=False)
















