from urllib.request import urlopen
from bs4 import BeautifulSoup
import string
import pandas as pd
import warnings
import os
from tqdm import tqdm

warnings.filterwarnings(action='ignore')

seasondf = pd.read_csv("season_info.csv")
# 숫자 앞 3자리가 클래스코드, 뒤 6자리가 선수코드

playerno = pd.read_csv("playerno.csv")

data = pd.DataFrame()
for i in tqdm(range(len(playerno))):
    na = []
    stat = []
    
    response = urlopen("https://fifaonline4.nexon.com/DataCenter/PlayerInfo?spid="+str(playerno["id"][i])+"&n1Strong=1")
    soup = BeautifulSoup(response, "html.parser")

    value = soup.find("div", {"class" : "player_view"})
    alldata = value.findAll('div', {"class" : "value"})
    allname = value.findAll('div', {"class" : "txt"})

    name_data = allname[-34:-1]
    status_data = alldata[-34:-1]
    
    season_num = playerno["id"][i]//1000000
    season = seasondf["season"][seasondf.index[seasondf["num"] == season_num][0]]

    for status in status_data:
        stat.append(int(status.text))
        
    for name in name_data:
        na.append(name.text)

    data.insert(i, season+playerno["name"][i], stat, allow_duplicates=True)
    

