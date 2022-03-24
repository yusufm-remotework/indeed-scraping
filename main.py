#How To Scraping https//indeed.com
import os
from turtledemo.chaos import h
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.indeed.com/jobs?q=Python%20Developer&l=New%20York&vjk=f0c41467acefa42d'
site = 'https://www.indeed.com'

params = {
    'q' : 'query',
    'l' : 'location'
}

headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}

res = requests.get(url, params=params, headers=headers)
#print(res.status_code)

soup = BeautifulSoup(res.text, 'html.parser')
#print(soup.prettify())

def get_total_pages():
    params ={
        'q':'query',
        'l':'location'
    }
    res = requests.get(url, params=params,headers=headers)

    #membuat library os
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    total_pages = []
    soup = BeautifulSoup(res.text, 'html.parser')
    pagination = soup.find('ul','pagination-list')
    pages =pagination.find_all('li')
    for page in pages:
        total_pages.append(page.text)

    max_page=int(max(total_pages))
    return max_page


def get_all_item():
    global company_name, company_link, title
    params = {
        'q':'query',
        'l': 'location'
    }
    res = requests.get(url,params=params, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = soup.find_all('table', 'jobCard_mainContent big6_visualChanges')
    #print(content)

    #pick item
    #title
    #company name
    #company link

    job_list=[]
    for item in content:
        title = item.find('h2', 'jobTitle').text
        company = item.find('span', 'companyName')
        company_name = company.text
        try:
            company_link = site + item.find('a')['href']
        except:
            company_link = 'link not available'
        company_location = item.find('div', 'companyLocation').text
        description = item.find('div', 'job-snippet')
        #print(description)

        #sorting data
        data_dict = {
            'title': title,
            'company_name': company_name,
            'link': company_link
        }
        job_list.append(data_dict)
    print(job_list)
    print(f'jumlah data: {len(job_list)}')

    #writing json file
    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass
    with open('json_result/job_list.json', 'w+') as data_json:
        json.dump(job_list, data_json)

    #create csv & excel
    df = pd.DataFrame(job_list)
    df.to_csv('indeed.csv', index=False)
    df.to_excel('indeed.xlsx', index=False)
    print('Data csv & excel created')





if '__name__=__main__':
    get_all_item()


