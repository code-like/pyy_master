import requests
import re
from bs4 import BeautifulSoup as bs
import xlwt
import time
from openpyxl import workbook 
from openpyxl import load_workbook
from urllib.parse import urlencode
import sys
import io
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding = 'utf-8')
def get_data(pages):
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
    k = 1
    wb = xlwt.Workbook()
    f = wb.add_sheet("招聘信息")
    raw = ['职位','公司','工作地点','薪资','更新时间']
    for i in range(len(raw)):
        f.write(0,i,raw[i])
    for i in range(1,pages):
        url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,"+ str(i)+".html"
        html = requests.get(url,headers = header).content
        #html.encoding = 'gbk'
        #html = response.content
        soup = bs(html,'lxml') 
        sp1 = soup.select('.t1 span a')
        sp2 = soup.select('.t2 a')
        sp3 = soup.select('.t3')
        sp4 = soup.select('.t4')
        sp5 = soup.select('.t5') 
        del(sp3[0])
        del(sp4[0]) 
        del(sp5[0])
        LocationList = []
        for j in range(len(sp2)):
            job = sp1[j].get('title')
            company = sp2[j].get('title')
            #f.write(codecs.Bom_UTF8)
            f.write(k,0,job)
            f.write(k,1,company)
            location = sp3[j].text
            LocationList.append(location)
            LocationGroup = np.array(LocationList)
            salary = sp4[j].text  
            timeupdate = sp5[j].text  
            f.write(k,2,location)
            f.write(k,3,salary)
            f.write(k,4,timeupdate)
            k += 1
        print(url)
        print("sleep 5 seconds , this is %s times" % i)
        time.sleep(5)
    wb.save('zhaoping.xlsx')
    print(LocationGroup)
    #print(location)
if __name__ == '__main__':
    #src = "https://search.51job.com/list/030200,000000,0000,00,9,99,Python,2,1.html"
    get_data(3)


