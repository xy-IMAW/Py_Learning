#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
#import bs4
import re


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
                Herf={}  
                # hrefs=li.find_all('a')['href']
                #match=li.next_element
                tags=li.find_all(tags_has_no_href)
                # date=li.get('data-time')
                #data.append(tags.contents)
                # for child in tags,children:
                #     data.append(child)
                hrefs=li.find_all('a')
                for href in hrefs:
                    Herf[href.string]=href.get('herf').text.strip()
                    #data.append(href.get('href'))
                data.append(Herf)
            except:
                pass
    return data

def tags_has_no_href(tag):
    return tag and not tag.has_attr('href')
data=main()
print(data)
   
   
           

