from BCRscraper.tests import *
from BCRscraper.propertyData import *
from Objects.Houses import *

for i in TakeData("https://ventadebienes.bancobcr.com/wps/portal/bcrb/bcrbienes/bienes/Casas/detalle/?codigo=6-167741-000&tipo_propiedad=1&descuento=1"):
    print("-"*10 + "\n"+i)

casa = House()
casa.id = 1
print(casa.id)

import re

justNumbers = lambda element: re.sub(r'[^0-9]', '', element)

def HCreator(Data):
    DataAUX=[]
    house = House()
    for i in Data:
        if "Folio" in i:
            house.id=justNumbers(i)
            print (i+"\n")
            print (house.id+"\n")

            


HCreator(TakeData("https://ventadebienes.bancobcr.com/wps/portal/bcrb/bcrbienes/bienes/Casas/detalle/?codigo=6-167741-000&tipo_propiedad=1&descuento=1"))