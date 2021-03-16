#!/usr/bin/python3
### am still working on this script

import requests
from bs4 import BeautifulSoup as bs

result = requests.get("https://people.cs.uct.ac.za/~lphiri/teaching/2015/csc1017f/slides/")
print(result.status_code)
print(result.headers)

src = result.content
#print(src)

soup = bs(src, features="html5lib")
links = soup.find_all("a")
#print(links)

domain = "https://people.cs.uct.ac.za"

def get_soup():
    return bs(requests.get(url).text, features="html5lib")

for link in links:
    if "pdf" in link.text:
        file_link = link.get_soup("href")
        print(file_link)
       # with open(link.text, "wb") as file:
       #     response = requests.get(domain + link)
       #     file.write(response.content)

       # print(link)
       # print(link.attrs['href'])
        
