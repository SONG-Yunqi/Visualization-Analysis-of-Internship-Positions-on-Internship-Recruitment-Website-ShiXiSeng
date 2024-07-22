import numpy as np
import pandas as pd
import requests
import re
import time
import csv

# get the urls for internships
df = pd.read_csv('urls for internships.csv')
urls = df['url']

# open a file to write new data in
file = open('internship data.csv', 'a', encoding = 'utf-8', newline = '')
writer = csv.writer(file)

# the features we want to know about an internship
colnames = ['name','company','city','day','salary','academic','duration','industry',
            'company_size','good_list','info']
writer.writerow(colnames)

file.close()

# set the request header
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'}

file = open('internship data.csv', 'a', encoding = 'utf-8', newline = '')
writer = csv.writer(file)

i = 0 # use i to count the number of internships we have processed

# crawl data for each internship
for url in urls:
    html = requests.get(url, headers = header)
    text = html.text
    
    i += 1
    
    # extract the features
    name = re.findall('"new_job_name" data-v-2bcf88a5><span data-v-2bcf88a5>(.*?)</span>',text)
    company = re.findall('.cname="(.*?)"',text)
    city = re.findall('"job_position" data-v-2bcf88a5>(.*?)</span>',text)
    day = re.findall('"job_week cutom_font" data-v-2bcf88a5>(.*?)</span>',text)
    salary = re.findall('"job_money cutom_font" data-v-2bcf88a5>(.*?)</span>',text)
    academic = re.findall('"job_academic" data-v-2bcf88a5>(.*?)</span>',text)
    duration = re.findall('"job_time cutom_font" data-v-2bcf88a5>(.*?)</span>',text)
    industry = re.findall('.industry="(.*?)"',text)
    company_size = re.findall('.scale="(.*?)"',text)
    goodlist = re.findall('"job_good_list" data-v-2bcf88a5><span data-v-2bcf88a5>(.*?)</span></div>',text)
    info = re.findall('.info="(.*?)"',text)
    
    crawler_result = [name,company,city,day,salary,academic,duration,industry,company_size,goodlist,info]
    features = []
    
    # integrate features
    for a in crawler_result:
        if a == []:
            features.append(None)
        else:
            features.append(a[0])
            
    # write features into csv file
    writer.writerow(features)
    
    if i % 100 == 0:
        time.sleep(5)
        print(i)

file.close()       

