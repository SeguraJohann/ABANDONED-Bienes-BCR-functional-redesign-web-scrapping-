import requests
from bs4 import BeautifulSoup
from selenium import webdriver



#Este script es solo para tomar los links de cada bien por página
def generaLinks(url):
    #url = 'https://ventadebienes.bancobcr.com/wps/portal/bcrb/bcrbienes/bienes/Casas?&tipo_propiedad=1'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    anchors = soup.find_all('div', {'class': 'table-cell cell100 bienImgBox'})

    elements = soup.find_all(class_='table-cell cell95 block-with-text')
    title = soup.find('title').get_text()
    description = soup.find('meta', attrs={'name': 'description'})['content']

    enlaces=[]

    for div in anchors:
        a_element = div.find('a')
        if a_element is not None:
            enlace = a_element['href']
            enlaces.append(['https://ventadebienes.bancobcr.com/'+ enlace])
  
    for i in range(0,len(enlaces)):
        enlaces[i].insert(0,elements[i].text.replace("\n", ""))
    return(enlaces)

def tomaDatos(url):
    #"table-cell cell42 detailTextSectionBox"
    response = requests.get(url)


    soup = BeautifulSoup(response.text, 'html.parser')
    container = soup.find('div', {"class":"table-cell cell42 detailTextSectionBox"})
    label_elements = container.find_all('label')
    for element in label_elements:
        print(element.text)

lista=generaLinks("https://ventadebienes.bancobcr.com/wps/portal/bcrb/bcrbienes/bienes/Casas?&tipo_propiedad=1")

#tomaDatos("https://ventadebienes.bancobcr.com/wps/portal/bcrb/bcrbienes/bienes/Casas/detalle/?codigo=2-491198-000&tipo_propiedad=1&descuento=1")

def recorrePáginas(url):

    # Configurar Selenium para usar un navegador Firefox
    driver = webdriver.Firefox()

    # Navegar a la página inicial
    driver.get(url)

    # Obtener el enlace para la página siguiente
    next_link = driver.find_element_by_css_selector('a.page-link[title="Siguiente"][href="#"]')

    # Mientras haya un enlace para la página siguiente, continuar navegando
    while next_link.get_attribute('href') != '#':

        # Obtener el contenido HTML de la página actual
        html = driver.page_source

        # Analizar el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')

        # Extraer la información deseada de la página actual

        # Hacer clic en el enlace para la página siguiente
        next_link.click()
    
'''
    # Esperar a que se cargue la página siguiente
    driver.implicitly_wait(10)

    # Obtener el enlace para la nueva página siguiente
    next_link = driver.find_element_by_css_selector('a.next')
     try:
        # Esperar a que el elemento con id="mi_div" aparezca en la página
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "mi_div"))
        )
    except:
        # Si el elemento no aparece después de 10 segundos, salir del bucle
        break

    # Cerrar el navegador al finalizar
    driver.quit()'''

def prueba():
    
    # Inicializar el navegador
    driver = webdriver.Chrome()

    # Cargar la página
    driver.get("https://ventadebienes.bancobcr.com/wps/portal/bcrb/bcrbienes/bienes/Casas?&tipo_propiedad=1")

    # Esperar a que cargue la página y se muestre la información
    driver.implicitly_wait(10)

    # Obtener todas las celdas de la tabla
    celdas_texto = driver.find_elements_by_css_selector(".table-cell.cell95.block-with-text")
    celdas_url = driver.find_elements_by_css_selector(".table-cell.cell100.bienImgBox a")

    # Crear una lista con el texto de cada celda
    texto_lista = [celda.text for celda in celdas_texto]

    # Crear una lista con las urls de cada imagen
    url_lista = [url.get_attribute("href") for url in celdas_url]

    # Imprimir los resultados
    print("Texto en las celdas:")
    for texto in texto_lista:
        print(texto)

    print("URLs de las imágenes:")
    for url in url_lista:
        print(url)

    # Cerrar el navegador
    driver.quit()

