import requests
from bs4 import BeautifulSoup
def TakeData(url):
    #"table-cell cell42 detailTextSectionBox"
    response = requests.get(url)


    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', {"class":"table-cell cell42 detailTextSectionBox"})
    label_elements = container.find_all('label')
    AllText=[]
    for element in label_elements:
        print(element.text)
        AllText.append(element.text)
    return(AllText)