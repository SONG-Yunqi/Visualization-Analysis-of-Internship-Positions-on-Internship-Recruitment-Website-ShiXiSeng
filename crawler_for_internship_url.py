# import packages
import numpy as np
import pandas as pd
import requests
import re
import time

# set the request header 
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

urls = []

# get the url for each internship on the summary website
# Crawl 500 pages of internships
for i in range(1,501): 
    
    # set the url for Page i of the summary website
    url_of_page_i = f'https://www.shixiseng.com/interns?page={i}&type=intern&keyword=&area=&months=&days=&degree=&official=&enterprise=&salary=-0&publishTime=&sortType=&city=%E5%85%A8%E5%9B%BD&internExtend='
    
    # request the website information
    html = requests.get(url_of_page_i,headers = header)
    
    # get the website text
    text = html.text
    
    # the url for each internship has a pattern 'https://www.shixiseng.com/intern/(.*?)pcm=pc_SearchList'
    a = re.findall('https://www.shixiseng.com/intern/(.*?)pcm=pc_SearchList',text)
    
    # get the complete urls
    for u in a:
        url = 'https://www.shixiseng.com/intern/' + u + 'pcm=pc_SearchList'
        urls.append(url)
    
    # pause regularly to avoid anti-crawler
    if i % 20 == 0:
        print(i)
        time.sleep(3)

# save the urls to CSV
df = pd.DataFrame({'url':urls})
df.to_csv('urls for internships.csv', index = False)  
