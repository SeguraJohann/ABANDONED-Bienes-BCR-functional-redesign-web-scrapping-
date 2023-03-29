import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time



def nextPage(url):
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(0.5)
    nextButton = driver.find_element(By.CLASS_NAME, "page-item.next").find_element(By.TAG_NAME, "a")
    print("A"*100)
    print(nextButton)
    nextButton.click()
    time.sleep(0.5)
    
nextPage("https://ventadebienes.bancobcr.com/wps/portal/bcrb/bcrbienes/bienes/Casas?&tipo_propiedad=1")