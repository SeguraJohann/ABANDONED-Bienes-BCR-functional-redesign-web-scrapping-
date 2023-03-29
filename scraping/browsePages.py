from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def existElement(source, ccsClass):
    try:
        source.find_element(By.CLASS_NAME, ccsClass).find_element(By.TAG_NAME, "a").is_displayed()
    except:
        return False
    return True

def nextPage(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(0.5)
 
    while(True):
        nextButton = driver.find_element(By.CLASS_NAME, "page-item.next").find_element(By.TAG_NAME, "a")
        html = driver.page_source

        print(getURLS(html))

        nextButton.click()
        time.sleep(1)

        if(existElement(driver,"page-item.next.disabled")):
            html = driver.page_source
            print(getURLS(html))
            break
    
def getURLS(html):
    #url = 'https://ventadebienes.bancobcr.com/wps/portal/bcrb/bcrbienes/bienes/Casas?&tipo_propiedad=1'

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

nextPage("https://ventadebienes.bancobcr.com/wps/portal/bcrb/bcrbienes/bienes/Casas?&tipo_propiedad=1")