#How To Scraping https//indeed.com

import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'

params = {
    'q': 'query',
    'l': 'location'
}

headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'}
res = requests.get (url, params=params, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
