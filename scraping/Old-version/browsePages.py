from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#Boolean function, Checks if a css Class element exists
def existElement(source, ccsClass):
    try:
        source.find_element(By.CLASS_NAME, ccsClass).find_element(By.TAG_NAME, "a").is_displayed()
    except:
        return False
    return True

#For each page, takes all urls and returns it as a list
#Input Selenium drivers
#Output Urls in the input (works only with one page)
def getURLS(html):

    soup = BeautifulSoup(html,'html.parser')

    anchors = soup.find_all('div', {'class': 'table-cell cell100 bienImgBox'})

    elements = soup.find_all(class_='table-cell cell95 block-with-text')

    enlaces=[]

    for div in anchors:
        a_element = div.find('a')
        if a_element is not None:
            enlace = a_element['href']
            enlaces.append(['https://ventadebienes.bancobcr.com'+ enlace])
  
    for i in range(0,len(enlaces)):
        enlaces[i].insert(0,elements[i].text.replace("\n", ""))
    return(enlaces) 

# Goes through each page of assets and return a list of ALL assets.
#To do: Make it return just the list
def nextPage(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(0.5)
    URLSList=[]
 
    while(True):
        nextButton = driver.find_element(By.CLASS_NAME, "page-item.next").find_element(By.TAG_NAME, "a")
        html = driver.page_source

        URLSList+=getURLS(html)

        nextButton.click()
        time.sleep(1)

        if(existElement(driver,"page-item.next.disabled")):
            html = driver.page_source
            URLSList+=getURLS(html)
            break
    return URLSList
    
