#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup


def main ():
    
    data = []
    soup=BeautifulSoup(open('2.html',encoding='utf-8'),'lxml')
    schedule = soup.find('div',class_='schedule_container left')
    boxs = schedule.find_all('div',class_='box')
   
    for i in range(0,1):        
        content=boxs[i].find('div',class_='content')
        # day=boxs[i].find('h2')
        # date=day.get('title')
        # data.append('\n'+date)
        lis=content.find_all('li')

        for li in lis:
            

            try:
                # hrefs=li.find_all('a')['href']
                match=li.strings[0]
                # date=li.get('data-time')
                data.append(match)
                hrefs=li.find_all('a')
                for href in hrefs:
                    
                    data.append(href.get('href')+href.string)
            except:
                pass
    return data

data=main()
print(data)
   
   
           

