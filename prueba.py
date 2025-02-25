import random
#Acciones
class informacionPersona:
    def __init__(self,nombre,pais):
      self.nombre = nombre
      self.pais = pais
nombre=str(input("Ingrese su nombre: "))
pais=str(input("ingrese su pais: "))
persona1 =informacionPersona(nombre,pais)


def elegirEvento():
    cantidad_eventos=int(input("Ingrese la cantidad de eventos: "))
    lista_eventos=[]

    for i in range (cantidad_eventos):
       nombreEvento =(input("Ingrese nombre del evento deportivo: "))
       lista_eventos.append(nombreEvento)

    if lista_eventos :
       evento_seleccionado=random.choice(lista_eventos)
       print(f"El evento seleccionado es: {evento_seleccionado}")
    else:
       print("Ningun evento fue seleccionado")
       
       




    

elegirEvento()




