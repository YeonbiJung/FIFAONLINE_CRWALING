from urllib.request import urlopen
from bs4 import BeautifulSoup
import string
import pandas as pd
seasondf = pd.read_csv("season_info.csv")
# 숫자 앞 3자리가 클래스코드, 뒤 6자리가 선수코드

playerno = pd.read_csv("playerno.csv")
data = pd.DataFrame()
    
response = urlopen("https://fifaonline4.nexon.com/DataCenter/PlayerInfo?spid=100001075&n1Strong=1")
soup = BeautifulSoup(response, "html.parser")
value = soup.find("div", {"class" : "player_view"})
alldata = value.findAll('div', {"class" : "value"})
allname = value.findAll('div', {"class" : "txt"})

name_data = allname[-34:-1]
status_data = alldata[-34:-1]

na=[]
stat = []
for status in status_data:
    stat.append(int(status.text))
    
for name in name_data:
    na.append(name.text)
    
print(na)