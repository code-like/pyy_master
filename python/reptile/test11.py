import requests
import re
from bs4 import BeautifulSoup as bs
from openpyxl import workbook
from openpyxl import load_workbook
from urllib.parse import urlencode
import sys
import io
import time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding = 'utf-8')
def get_data(pages):
    job = []  
    location = [] 
    company = [] 
    salary = [] 
    updatetime = []
    for j in range(pages):
        url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,"+ str(j)+".html"
        html = requests.get(url).content   
        soup = bs(html,'lxml')  
        for soup in soup.find_all("div",{"class":"el"}):
            joblist = soup.find_all("p",class_="t1")
            print(joblist)
            companylist = soup.find_all("span",class_="t2")
            locationlist = soup.find_all("span",class_="t3")
            salarylist = soup.find_all("span",class_="t4") 
            timelist = soup.find_all("span",class_="t5")
            #print(joblist)
            for jobs in joblist:
                j = jobs.find_all("a",target="_blank")
                a = j[0].get_text()
                job.append(a)
                #print(a)
            for companys in companylist:
                company.append(companys.text)
            for locations in locationlist:
                location.append(locations.text)
            for salarys in salarylist:
                salary.append(salarys.text)
            for times in timelist:
                updatetime.append(times.text)
    for m in range(len(job)):
        ws.append([job[m],company[m],location[m],salary[m],updatetime[m]])
            
if __name__ == '__main__':
    wb = workbook.Workbook()
    ws = wb.active
    get_data(2)
    wb.save('python_job.xlsx')
