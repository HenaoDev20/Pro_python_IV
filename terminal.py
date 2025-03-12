
def ingresar_informacion_viaje():
    viajes = []  
    
    while True:
     try:
        cant_viajes = int(input("Ingrese la cantidad de viajes: "))
        if cant_viajes < 0:
            print('La cantidad de viajes no puede ser negativa')
        else:
            break
     except ValueError:
        print('La cantidad de viajes debe ser un número válido')

       
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
            try:
             costo_pasaje = float(input("Ingresar el costo del pasaje: "))
             if costo_pasaje < 0:
                 print("El costo del pasaje no puede ser negativo")
             else:
                break
            except ValueError:
             print("No se pueden ingresar letras, solo números")


        pasajeros = []
        while True:
         try:
             cant_pasajeros = int(input("Ingrese la cantidad de pasajeros: "))
             if cant_pasajeros < 0:
              print('La cantidad de viajes no puede ser negativa')
             else:
                break
         except ValueError:
            print('La cantidad de viajes debe ser un número válido')

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
                 edad_pasajero = int(input("Ingresar la edad del pasajero: "))
                 if edad_pasajero < 0:
                   print("No se pueden ingresar números negativos")
                 else:
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


#1
def total_pasajeros(viajes):
    pasajeros_totales = 0
    for viaje in viajes:
        pasajeros_totales += len(viaje["pasajeros"]) 
    return pasajeros_totales
#2
def total_dinero_recaudado(viajes):
    total_dinero_recaudado= 0
    for viaje in viajes:
        total_dinero_recaudado += viaje["costo"] * len(viaje["pasajeros"]) 
    return total_dinero_recaudado
#3
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
#4
def total_descuento_estudiantes(viajes):
    total_descuento = 0

    for viaje in viajes:
        costo = viaje["costo"]
        for pasajero in viaje["pasajeros"]:
            if pasajero["estudiante"] == "s":
                descuento = costo * 0.30
                total_descuento += descuento

    return total_descuento
 #5
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
#6
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
#7

def promedio_edad_mujeres(viajes):
    sum_edades_mujeres=0
    total_mujeres=0
    for viaje in viajes:
        for pasajero in viaje["pasajeros"]:
            if pasajero["genero"]=="f":
             sum_edades_mujeres += int(pasajero["edad"])
             total_mujeres += 1
             if total_mujeres >0:
              promedio = sum_edades_mujeres/total_mujeres
            print(f"El promedio de edad de las mujeres es: {promedio}")
            
       

def mostrar_informacion_completa():
    viajes = ingresar_informacion_viaje()

    print("\n Informacion del viaje y sus pasajeros :")
   
    for i, viaje in enumerate(viajes):
        print(f"\nViaje {i+1}: De {viaje['origen']} a {viaje['destino']} - Costo: ${viaje['costo']}")



        if viaje["pasajeros"]:
            print("Pasajeros:")
            for j, pasajero in enumerate(viaje["pasajeros"]):
                print(f"  - Pasajero {j+1}: {pasajero['nombre']}, {pasajero['edad']} años, Género: {pasajero['genero']}, Es estudiante: {pasajero['estudiante']}")
        else:
            print("  No hay pasajeros en este viaje.")
     #1       
    print(f"Total de pasajeros: {total_pasajeros(viajes)}")
     #2
    print(f"Total de dinero recaudado:{total_dinero_recaudado(viajes)}")
    #3
    mujeres, hombres = total_dinero_por_genero(viajes)
    print(f"Total recaudado por mujeres: ${mujeres}")
    print(f"Total recaudado por hombres: ${hombres}")
    #4
    descuento_total = total_descuento_estudiantes(viajes)
    print(f"Total de descuento aplicado a los pasajeros estudiantes: ${descuento_total:}")
    #5
    viaje_mayor_recaudacion(viajes)
    #6
    promedio_edad_pasajeros(viajes)
    #7
    promedio_edad_mujeres(viajes)




mostrar_informacion_completa()




   
            
            
    
       

  

    





