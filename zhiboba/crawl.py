#-*- coding:utf-8 -*-
import bs4
import requests

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=3)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text   
    except:
        return "Someting Wrong！"+r.status_code

def getmatch(url):
    html=getHtmlText(url)
    
    #soup = bs4.BeautifulSoup(open('zhiboba/demo.html',encoding='utf-8'),'lxml')
    soup=bs4.BeautifulSoup(html,'lxml')
    date=soup.find('div',class_='box').div.h2.text
    boxs=soup.find_all('div',attrs={'class':'content'})
    print (date)
    litags=boxs[0].find_all('li')
    for j in range(0,len(litags)):
        hrefs=litags[j].find_all('a')        
        match=litags[j].contents[0]
        if litags[j].span:
            if litags[j].img:
                img=litags[j].find_all('img')
                if litags[j].b.img:
                    #<b>标签包含<img>
                    match=match+'\t'+litags[j].b.text 
                else:
                    #<b>标签不包含<img>                
                    match=match+'\t'+litags[j].b.text+img[0].previous_element+litags[j].span.text+img[1].next_element
            else:
                match=match+'\t'+litags[j].span.text+litags[j].span.next.next_element
        else:
            pass
            
        print (match)
        
        for i in range(0,len(hrefs)):
        #print (href.text)
        #print (href.)
            print ( hrefs[i].text+':\t' +'http://www.zhiboba.cc'+ hrefs[i]['href'] )    
            
        


def W2File(data):
    with open('ZhiboLink.txt','a+',encoding='utf-8') as f:
        for one in data:
            f.write(one+'\n')
    
    print('数据写入完毕！')
'''
urls = []



data=getmatch(url)
W2File(data)
'''
'''
    #多个日期的content div
    for t in range(0,len(boxs)):        
        
'''
url='https://www.zhibo8.cc/'
getmatch(url)