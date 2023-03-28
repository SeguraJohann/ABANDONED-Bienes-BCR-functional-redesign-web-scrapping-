import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def getUrls(url):

    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    time.sleep(0.5)
    response = requests.get(url)
    nextButton = driver.find_element(By.CLASS_NAME, "page-item.next").find_element(By.TAG_NAME, "a")
    print("A"*100)
    print(nextButton)
    nextButton.click()
    time.sleep(0.5)
    
getUrls("https://ventadebienes.bancobcr.com/wps/portal/bcrb/bcrbienes/bienes/Casas?&tipo_propiedad=1")