import random
#Acciones

def registroEvento():
    cantidad_participantes =int(input("Ingrese la cantidad de participantes: "))
    nombre_participantes=[]
    pais_participantes =[]
    
    for i in range(cantidad_participantes):
       nombre_participante =(input("Ingrese el nombre del participante: "))
       pais_participante=(input("Ingrese pais del participante: "))
       nombre_participantes.append(nombre_participante)
       pais_participantes.append(pais_participante)

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
       
registroEvento()




