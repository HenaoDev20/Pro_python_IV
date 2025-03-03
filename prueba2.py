#Una empresa de transporte de pasajeros lo ha contratado a usted para desarrollar un sistema para gestionar sus viajes.

#El sistema debe permitir:
    #- Ingresar datos de diferentes viajes, es decir, se pueden tener múltiples viajes en el sistema, no solamente uno.
    #- Por cada viaje se debe ingresar
        #- Ciudad de origen
        #- Ciudad de destino
        #- Precio del viaje
        #- Cantidad de pasajeros
        #- Por cada pasajero se debe ingresar:
            #- Nombre del pasajero
            #- Género del pasajero
            #- Si el pasajero es estudiante, tiene un descuento del 30% en el precio del viaje
    #- Por cada viaje se pueden ingresar una cantidad indeterminada de pasajeros. Por ejemplo, un viaje puede tener
    #5 pasajeros, otro 10 pasajeros, otro 2 pasajeros, etc.
    #- Al final el sistema debe permitir mostrar la siguiente información:
        #- Total de pasajeros que viajaron
        #- Total de dinero recaudado
        #- Total de dinero recaudado por género, es decir, total de dinero recaudado por hombres y total de dinero recaudado por mujeres
        #- El total de descuentos aplicados a los pasajeros estudiantes
        #- Cual fue el viaje que recaudó más dinero y cuanto dinero recaudó
   #- El promedio de edad de los pasajeros

def ingresar_informacion_viaje():
    viajes=[]
    cant_viajes = int(input("Ingrese la cantidad de viajes: "))

    for i in range(cant_viajes): 
        print(f"Viaje {i+1}")
        

        while True:  
            c_origen = input("Ingresar la ciudad de origen: ")
            try:
                if float(c_origen):  
                    print("No se puede ingresar un número como ciudad")
            except ValueError:
                if c_origen == "":  
                    print("Este campo no puede estar vacio")
                else:
                    print(f"Ciudad de origen registrada: {c_origen}")
                break 

        while True:
            c_destino =input("Ingresar la ciudad de destino: ")
            try:
                if float(c_destino):  
                    print("No se puede ingresar un número como ciudad")
            except ValueError:
                if c_destino =="":
                    print("Este campo no puede estar vacio")
                else:
                     print("Ciudad de destino registrada")
                break
        
        while True:
           costo_pasaje=input("Ingresar el costo del pasaje: ")
           try:
               if float(costo_pasaje):
                   print (f"El costo es:{costo_pasaje} ")
                   break
           except ValueError:
                   print("No se pueden ingresar letras")

        viajes.append({
            "origen": c_origen,
            "destino": c_destino,
            "costo": costo_pasaje
        })

        return viajes
           
def ingresar_informacion_pasajero():

    pasajeros=[]
    cant_pasajeros = int(input("Ingrese la cantidad de pasajeros")) 

    for i in range(cant_pasajeros):
        print(f"Pasajero {i+1}")

        while True:
            nom_pasajero=(input("Ingrese el nombre del pasajero: "))
            try:
                if float(nom_pasajero or nom_pasajero==""):
                    print("No se puede ingrear un numero como nombre, tampoco dejar campo vacio...")
            except ValueError:
                print(f"El nombre del pasajero es: {nom_pasajero}")
                break

        while True:
           edad_pasajero=input("Ingresar la edad del pasajero: ")
           try:
               if float(edad_pasajero):
                   print (f"La edad del pasajero es:{edad_pasajero} ")
                   break
           except ValueError:
                   print("No se pueden ingresar letras solo números")

        while True:
            genero_pasajero=input("Ingrese el genero del pasajero: ")
            try:
                if(genero_pasajero== "M"):
                    print("El genero es masculino")
                    break
            except ValueError:
                print("Si es hombre solo puede ingresar |M o F|")
               
            
        pasajeros.append({
            "nombre": nom_pasajero,
            "edad": edad_pasajero,
            "genero": genero_pasajero
        })

        return pasajeros  

def mostrar_informacion_completa():
    viajes = ingresar_informacion_viaje()
    pasajeros = ingresar_informacion_pasajero()

    print("\n RESUMEN DE VIAJES Y PASAJEROS:")
    for i, viaje in enumerate(viajes):
        print(f"\n Viaje {i+1}: De {viaje['origen']} a {viaje['destino']} - Costo: ${viaje['costo']}")

    for i, pasajero in enumerate(pasajeros):
        print(f"\n Pasajero {i+1}: {pasajero['nombre']}, {pasajero['edad']} años, Género: {pasajero['genero']}")



mostrar_informacion_completa()


   
            
            
    
       
#def ingresar_informacion_pasajero():
  

    





