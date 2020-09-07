import urllib
from time import sleep
import os 
from selenium import webdriver
from bs4 import BeautifulSoup

search = input("검색어를 입력하세요 : ")
search = urllib.parse.quote(search)

url = 'https://www.instagram.com/explore/tags/'+str(search)+'/'

# driver 크롬드라이버 주소
driver = webdriver.Chrome() 
driver.get(url)
sleep(5)

SCROLL_PAUSE_TIME = 3.0
links = set()
cnt = 0
# limit 원하는 게시물 갯수
limit = 5000 


while True:
    pageString = driver.page_source
    bsObj = BeautifulSoup(pageString,"lxml")
    
    for link in bsObj.find_all(name="div",attrs={"class" : "Nnq7C weEfm"}):
        info = link.select('a')[0]
        href = info.attrs['href']
        links.add(href)
        info = link.select('a')[1]
        href = info.attrs['href']
        links.add(href)
        info = link.select('a')[2]
        href = info.attrs['href']
        links.add(href)
    if len(links) >= limit:
        break 

        
        
    last_height = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height== last_height:
            break
        else:
            last_height = new_height
            continue

wording = []
for link in links:
    URL = 'https://www.instagram.com'+link
    driver.get(URL)
    sleep(2)
    pageString = driver.page_source
    bsObj = BeautifulSoup(pageString,"lxml")
    temp = bsObj.find(name="div",attrs={"class":"C4VMK"})
    if temp == None:
        continue
    temp1 = temp.find("span")
    temp1 = temp1.text
    temp1 = temp1.replace("\u2063",'')
    wording.append(temp1)
    
print("finished") 
