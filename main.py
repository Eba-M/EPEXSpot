from bs4 import BeautifulSoup
import requests

main_url = "https://www.epexspot.com/en/market-data?market_area=DE-LU&delivery_date=2024-12-31&modality=Auction&sub_modality=DayAhead&product=60&data_mode=table"
print (main_url)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Ch$
req = requests.get(main_url,headers=headers)
print (req.text)
soup = BeautifulSoup(req.text, "html.parser")
# Finding the main title tag.
title = soup.find("table", class_="table-01 table-length-1")
line = title.contents
print(len(line))

td = title.find_all("tr", class_="child")
# für jedes Element
y = 0;
for x in td:
        print(y,end=' ');print(x.contents[7].string)
        y=y+1

