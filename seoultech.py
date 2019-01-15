# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from datetime import datetime

url="http://www.seoultech.ac.kr/"

req = requests.get(url)
html = req.text

soup = BeautifulSoup(html,'html.parser')
templist = soup.select('div.class="t14">div>ul>li')
print(templist)
# a=[]

# for temp in templist:
#     a.append(temp.text)

# # j=1

# list_rank = []
# num = 1
# for i in a:
#     if num>9:
#         list_rank.append(i[5:-2])
#     else:
#         list_rank.append(i[4:-2])
#     num += 1
# for s, list in enumerate (list_rank):
#     print(str(s+1)+"위"+list)
