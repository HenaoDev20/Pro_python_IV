
def ingresar_informacion_viaje():
    viajes = []  
    
    while True:
        try:
            cant_viajes = int(input("Ingrese la cantidad de viajes: "))
            break
        except ValueError:
            print("Solo puede ingresar números")

    for i in range(cant_viajes): 
        print(f"\nViaje {i+1}")

        while True:  
            c_origen = input("Ingresar la ciudad de origen: ")
            if c_origen== "":
                print("Este campo no puede estar vacío")
            elif c_origen.isnumeric():
                print("No se puede ingresar un número como ciudad")
            else:
                break
            
        while True:
            c_destino = input("Ingresar la ciudad de destino: ")
            if c_destino== "":
                print("Este campo no puede estar vacío")
            elif c_destino.isnumeric():
                print("No se puede ingresar un número como ciudad")
            else:
                break

        while True:
            costo_pasaje = input("Ingresar el costo del pasaje: ")
            try:
                costo_pasaje = float(costo_pasaje)
                break
            except ValueError:
                print("No se pueden ingresar letras, solo números")

        pasajeros = []
        while True:
            try:
                cant_pasajeros = int(input(f"Ingrese la cantidad de pasajeros para el viaje: "))
                break
            except ValueError:
                print("Ingrese un número válido")

        for j in range(cant_pasajeros):
            print(f"\nPasajero {j+1}")
            while True:
                nom_pasajero = input("Ingrese el nombre del pasajero: ")
                if nom_pasajero == "":
                    print("El nombre no puede estar vacío")
                elif nom_pasajero.isnumeric():
                    print("No se puede ingresar un número como nombre")
                else:
                    break

            while True:
                try:
                    edad_pasajero = input("Ingresar la edad del pasajero: ")
                    break
                except ValueError:
                    print("No se pueden ingresar letras, solo números")

            while True:
                genero_pasajero = input("Ingrese el género del pasajero (m o f): ")
                if genero_pasajero in ["m", "f"]:
                    break
                else:
                    print("Debe ingresar 'm' o 'f'")
            
            while True:
                pasajero_estudiante=input("Si el pasajero es estudiante ingresar |s| sino |n|" )
                if pasajero_estudiante in['s','n']:
                    break
                else:
                    print("Debe ingresar |s| o |n|")

            pasajeros.append({
                "nombre": nom_pasajero,
                "edad": edad_pasajero,
                "genero": genero_pasajero,
                "estudiante": pasajero_estudiante
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

def total_dinero_por_genero(viajes):
    total_mujeres = 0
    total_hombres = 0

    for viaje in viajes:
        costo = viaje["costo"]
        for pasajero in viaje["pasajeros"]:
            if pasajero["genero"] == "f":
                total_mujeres += costo
            elif pasajero["genero"] == "m":
                total_hombres += costo

    return total_mujeres, total_hombres

def total_descuento_estudiantes(viajes):
    total_descuento = 0

    for viaje in viajes:
        costo = viaje["costo"]
        for pasajero in viaje["pasajeros"]:
            if pasajero["estudiante"] == "s":
                descuento = costo * 0.30
                total_descuento += descuento

    return total_descuento
 
def viaje_mayor_recaudacion(viajes):
    mayor_recaudacion = 0
    viaje_mayor = None

    for viaje in viajes:
        recaudacion = viaje["costo"] * len(viaje["pasajeros"])
        if recaudacion > mayor_recaudacion:
            mayor_recaudacion = recaudacion
            viaje_mayor = viaje

    if viaje_mayor:
        print(f"\n El viaje que más recaudó fue de {viaje_mayor['origen']} a {viaje_mayor['destino']}, recaudo en total: ${mayor_recaudacion:}")
    else:
        print("\nNo hay viajes registrados.")

def promedio_edad_pasajeros(viajes):
    suma_edades = 0
    total_pasajeros = 0

    for viaje in viajes:
        for pasajero in viaje["pasajeros"]:
            suma_edades += int(pasajero["edad"])
            total_pasajeros += 1

    if total_pasajeros > 0:
        promedio = suma_edades / total_pasajeros
        print(f"\n El promedio de edad de los pasajeros es: {promedio:} años")
    else:
        print("\nNo hay pasajeros registrados.")


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
                print(f"  - Pasajero {j+1}: {pasajero['nombre']}, {pasajero['edad']} años, Género: {pasajero['genero']}, Es estudiante: {pasajero['estudiante']}")
        else:
            print("  No hay pasajeros en este viaje.")
            
    print(f"Total de pasajeros: {total_pasajeros(viajes)}")

    print(f"Total de dinero recaudado:{total_dinero_recaudado(viajes)}")

    mujeres, hombres = total_dinero_por_genero(viajes)
    print(f"Total recaudado por mujeres: ${mujeres}")
    print(f"Total recaudado por hombres: ${hombres}")

    descuento_total = total_descuento_estudiantes(viajes)
    print(f"Total de descuento aplicado a los pasajeros estudiantes: ${descuento_total:}")

    viaje_mayor_recaudacion(viajes)

    promedio_edad_pasajeros(viajes)



mostrar_informacion_completa()




   
            
            
    
       

  

    





