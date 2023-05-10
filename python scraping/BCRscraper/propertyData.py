import requests
from bs4 import BeautifulSoup
isEmpty = lambda element : (element == "")
def TakeData(url):
    #"table-cell cell42 detailTextSectionBox"
    response = requests.get(url)


    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', {"class":"table-cell cell42 detailTextSectionBox"})
    container = (container.get_text())
    container = container.split("\n")
    aux = []
    for i in container:
        if(not isEmpty(i)):
            aux.append(i)
    return aux

#for i in TakeData("https://ventadebienes.bancobcr.com/wps/portal/bcrb/bcrbienes/bienes/Casas/detalle/?codigo=6-167741-000&tipo_propiedad=1&descuento=1"):
#    print("<" +i.replace("\n", "") + ">")