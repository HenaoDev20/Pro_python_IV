class Inmueble:
    inmueble_list=[]

    def __init__(self,nombre,proposito,precio):
        self.nombre = nombre
        self.proposito =proposito
        self.precio=precio
        Inmueble.inmueble_list.append(self)

    @property
    def nombre(self):
         return self._nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        if isinstance(nuevo_nombre,str) and not nuevo_nombre.isdigit():
            self._nombre=nuevo_nombre
        else:
            raise ValueError("Nombre no valido")
        

can_registros = int(input("Ingrese la cantidad de registros de inmueble: "))
        
for i in range(can_registros):
    print(f"\nRegistro {i+1}:")
    while True:
        try:
            nombre = input("Ingrese el nombre del inmueble: ")
            proposito = input("Ingrese el proposito del inmueble: ")
            precio = float(input("Ingrese el precio del inmueble: "))
            inmueble = Inmueble(nombre, proposito, precio)
            break
        except ValueError as e:
            print(e)
            print("Por favor ingrese un nombre válido")

           

if Inmueble.inmueble_list:
    print("\nLista de inmuebles registrados:")
    for inmueble in Inmueble.inmueble_list:
          print(f"-- Nombre: {inmueble.nombre} | proposito: {inmueble.proposito} | Precio: ${inmueble.precio}")
else:
    print("\nNo hay inmuebles registrados.")







