class Inmueble:
    inmueble_list = []

    def __init__(self, nombre, proposito, precio):
        self.nombre = nombre
        self.proposito = proposito
        self.precio=precio
        Inmueble.inmueble_list.append(self)

    @staticmethod
    def validar_nombre(nombre):
        if not isinstance(nombre, str) or nombre.isdigit():
            raise ValueError("Nombre no válido:")
        elif nombre=="":
            raise ValueError("Nombre Válido")

    @staticmethod
    def validar_proposito(proposito):
        if not isinstance(proposito, str) or proposito.isdigit():
            raise ValueError("Propósito no válido:")
        elif proposito=="":
            raise ValueError("Proposito no Válido")
    
    @staticmethod
    def validar_precio(precio):
        if precio == "":
          raise ValueError("Precio no válido: No puede estar vacío.")
        try:
            float(precio)  
        except ValueError:
           raise ValueError("Precio no válido: Debe ser un número.")

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        Inmueble.validar_nombre(nuevo_nombre)
        self._nombre = nuevo_nombre

    @property
    def proposito(self):
        return self._proposito
    @proposito.setter
    def proposito(self, nuevo_proposito):
        Inmueble.validar_proposito(nuevo_proposito)
        self._proposito = nuevo_proposito
    
    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self,nuevo_precio):
        Inmueble.validar_precio(nuevo_precio)
        self._precio = nuevo_precio



can_registros = int(input("Ingrese la cantidad de registros de inmuebles: "))

for i in range(can_registros):
    print(f"\nRegistro {i+1}:")

    while True:
        try:
            nombre = input("Ingrese el nombre del inmueble: ")
            Inmueble.validar_nombre(nombre)
            break
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")

    while True:
        try:
            proposito = input("Ingrese el propósito del inmueble: ")
            Inmueble.validar_proposito(proposito)
            break
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")
    
    while True:
        try:
            precio =float(input("Ingrese el precio del Inmueble: "))
            Inmueble.validar_precio(precio)
            break
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")
            
    inmueble = Inmueble(nombre, proposito, precio)

print("\nLista de Inmuebles Registrados:")
for inmueble in Inmueble.inmueble_list:
    print(f"-- Nombre: {inmueble.nombre}|Propósito: {inmueble.proposito}|Precio: {inmueble.precio}")
