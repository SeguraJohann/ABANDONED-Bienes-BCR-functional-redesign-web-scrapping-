from BCRscraper.tests import *
from BCRscraper.propertyData import *
from Objects.Houses import *
import re



#for i in TakeData("https://ventadebienes.bancobcr.com/wps/portal/bcrb/bcrbienes/bienes/Casas/detalle/?codigo=6-167741-000&tipo_propiedad=1&descuento=1"):
#    print("-"*10 + "\n"+i)



def justFloats(element):
    #Allowed = '0123456789,,'
    #result = ''.join(caracter for caracter in element if caracter in Allowed)
    #result=""
    #print("check fun")
    #for i in element:
    #    print (i+"\n")
    #    print (i in Allowed +"\n")
    #    if (i in Allowed):
    #        result = result + i
    #    print (result +"\n")
    if ("," in element):
        return float(justInt(element))/100
    return element

justInt = lambda element: re.sub(r'[^0-9]', '', element)
makeBool = lambda element: "Sí" in element

def HCreator(Data):
    house = House()
    for i in Data:
        if "Folio" in i:
            house.id=justInt(i)
            print (i+"\n")
            print (">"+house.id+"\n")

        elif "Condominio" in i:
            house.condominium=makeBool(i)
            print (i+"\n")
            print (">"+"Condominio "+str(house.condominium)+"\n")

        elif "Plantas" in i:
            house.floors=justInt(i)
            print (i+"\n")
            print (">"+"Plantas "+str(house.floors)+"\n")

        elif "Cochera" in i:
            house.garage=makeBool(i)
            print (i+"\n")
            print (">"+str(house.garage)+"\n")
            
        elif "Habitaciones" in i:
            house.rooms=justInt(i)
            print (i+"\n")
            print (">"+"Habitaciones "+str(house.rooms)+"\n")
            
        elif "Baños" in i:
            house.bathrooms=justInt(i)
            print (i+"\n")
            print (">"+"Baños "+str(house.bathrooms)+"\n")

        elif "Terraza" in i:
            house.terrace=makeBool(i)
            print (i+"\n")
            print (">"+str(house.terrace)+"\n")

        elif "Pilas" in i:
            house.batteryroom=makeBool(i)
            print (i+"\n")
            print (">"+str(house.batteryroom)+"\n")

        elif "Servicio" in i:
            house.maidsroom=makeBool(i)
            print (i+"\n")
            print (">"+str(house.maidsroom)+"\n")

        elif "Zona Verde" in i:
            house.greenarea=makeBool(i)
            print (i+"\n")
            print (">"+str(house.greenarea)+"\n")

        elif "Piscina" in i:
            house.pool=makeBool(i)
            print (i+"\n")
            print (">"+str(house.pool)+"\n")

        elif "Frente" in i:
            house.front=justFloats(i)
            print (i+"\n")
            print (">"+"Frente "+str(house.front)+"\n")

        elif "Fondo" in i:
            house.dept=justFloats(i)
            print (i+"\n")
            print (">"+"Fondo "+str(house.dept)+"\n")

        elif "área del terreno" in i:
            house.area=justFloats(i)
            print (i+"\n")
            print (">"+"Condominio "+str(house.area)+"\n")

        elif "área de construcción" in i:
            house.builtArea=justFloats(i)
            print (i+"\n")
            print (">"+"Condominio "+str(house.builtArea)+"\n")

        elif "precio inicial" in i:
            house.inPrice=justFloats(i)
            print (i+"\n")
            print (">"+"Condominio "+str(house.inPrice)+"\n")

        elif "precio de venta final" in i:
            house.finPrice=justFloats(i)
            print (i+"\n")
            print (">"+"Condominio "+str(house.finPrice)+"\n")




#HCreator(TakeData("https://ventadebienes.bancobcr.com/wps/portal/bcrb/bcrbienes/bienes/Casas/detalle/?codigo=6-167741-000&tipo_propiedad=1&descuento=1")) 
#HCreator(TakeData("https://ventadebienes.bancobcr.com/wps/portal/bcrb/bcrbienes/bienes/Casas/detalle/?codigo=4-106506-000&tipo_propiedad=1&descuento=1"))