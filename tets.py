import requests
import time
from bs4 import BeautifulSoup

def get_agent():
    '''
    模拟header的user-agent字段，
    返回一个随机的user-agent字典类型的键值对
    '''
    agents = ['Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
              'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)']
    fakeheader = {}
    fakeheader['User-agent'] = random.choice(agents)
    #agents[random.randint(0, len(agents))]   
    return fakeheader

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=3)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text   
    except:
        return "Someting Wrong！"+r.status_code

def get_one_data(url):
    
    data = []
    html = getHtmlText(url)
    soup = BeautifulSoup(html,'lxml')
    schedule = soup.find('div',class_='schedule_container left')
    boxs = schedule.find_all('div',class_='box')
   
    for box in boxs:        
        content=box.find('div',class_='content')
        day=box.find('h2')
        date=day.get('title')
        data.append('\n'+date)
        lis=content.find_all('li')

        for li in lis:
            #hrefs=li.find_all('a')['href']

            try:
                #date=li['datetime']
                match=li.text

                data.append(match)
            except:
                pass
    return data
     
    

    
def W2File(data):
    with open('3.txt','a+',encoding='utf-8') as f:
        for one in data:
            f.write(one+'\n')
    
    print('数据写入完毕！')

urls = []

url='https://www.zhibo8.cc/'

data=get_one_data(url)
W2File(data)
