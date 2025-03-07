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
    viajes = []
    cant_viajes = int(input("Ingrese la cantidad de viajes: "))

    for i in range(cant_viajes): 
        print(f"\nViaje {i+1}")
        while True:  
            c_origen = input("Ingresar la ciudad de origen: ")
            try:
                if float(c_origen):  
                    print("No se puede ingresar un número como ciudad")
            except ValueError:
                if c_origen == "":  
                    print("Este campo no puede estar vacío")
                else:
                    print(f"Ciudad de origen registrada exitosamente...")
                    break  

        while True:
            c_destino = input("Ingresar la ciudad de destino: ")
            try:
                if float(c_destino):  
                    print("No se puede ingresar un número como ciudad")
            except ValueError:
                if c_destino == "":
                    print("Este campo no puede estar vacío")
                else:
                    print(f"Ciudad de destino registrada exitosamente")
                    break

        while True:
            costo_pasaje = input("Ingresar el costo del pasaje: ")
            try:
                costo_pasaje = float(costo_pasaje)
                print(f"El costo es: {costo_pasaje}")
                break
            except ValueError:
                print("No se pueden ingresar letras, solo números")

        # Registrar pasajeros para este viaje
        pasajeros = []
        cant_pasajeros = int(input(f"\nIngrese la cantidad de pasajeros para el viaje: "))
       

        for j in range(cant_pasajeros):
            print(f"\nPasajero {j+1}")

            while True:
                nom_pasajero = input("Ingrese el nombre del pasajero: ")
                try:
                    if float(nom_pasajero):  
                        print("No se puede ingresar un número como nombre")
                except ValueError:
                    if nom_pasajero == "":
                        print("El nombre no puede estar vacío")
                    else:
                        print(f"El nombre del pasajero registrado exitosamente...")
                        break

            while True:
                edad_pasajero = input("Ingresar la edad del pasajero: ")
                try:
                    edad_pasajero = int(edad_pasajero)
                    print(f"La edad del pasajero registrada exitosamente...")
                    break
                except ValueError:
                    print("No se pueden ingresar letras, solo números")

            while True:
                try:
                    genero_pasajero = input("Ingrese el género del pasajero (m o f): ")
                    if (genero_pasajero == "m" ) :
                        print(f"El género es masculino{genero_pasajero}")
                    elif(genero_pasajero== "f"):
                        print(f"El genero es :{genero_pasajero}")
                    break
                except ValueError:
                    print("Debe ingresar 'm' o 'f'")
             

            pasajeros.append({
                "nombre": nom_pasajero,
                "edad": edad_pasajero,
                "genero": genero_pasajero
            })
           

        viajes.append({
            "origen": c_origen,
            "destino": c_destino,
            "costo": costo_pasaje,
            "pasajeros": pasajeros
        })

    return viajes  


def total_pasajeros(viajes):
    pasajeros_totales = 0
    for viaje in viajes:
        pasajeros_totales += len(viaje["pasajeros"]) 
    return pasajeros_totales

def total_dinero_recaudado(viajes):
    total_dinero_recaudado= 0
    for viaje in viajes:
        total_dinero_recaudado += viaje["costo"] * len(viaje["pasajeros"]) 
    return total_dinero_recaudado
  
def mostrar_informacion_completa():
    viajes = ingresar_informacion_viaje()

    print("\n Informacion del viaje y sus pasajeros :")
    #En cada vuelta del for, Python toma un diccionario de la lista viajes y lo asigna a la variable viaje automáticamente.
    for i, viaje in enumerate(viajes):
        print(f"\nViaje {i+1}: De {viaje['origen']} a {viaje['destino']} - Costo: ${viaje['costo']}")


#Si "pasajeros" contiene una lista con elementos (o sea, hay pasajeros), la condición es True y entra al if.
        if viaje["pasajeros"]:
            print("Pasajeros:")
            for j, pasajero in enumerate(viaje["pasajeros"]):
                print(f"  - Pasajero {j+1}: {pasajero['nombre']}, {pasajero['edad']} años, Género: {pasajero['genero']}")
        else:
            print("  No hay pasajeros en este viaje.")
            
    print(f"Total de pasajeros: {total_pasajeros(viajes)}")
    print(f"Total de dinero recaudado:{total_dinero_recaudado(viajes)}")


mostrar_informacion_completa()




   
            
            
    
       

  

    





