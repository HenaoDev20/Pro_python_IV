class Inmueble:
    inmueble_list = []

    def __init__(self, nombre, proposito, precio):
        self.nombre = nombre
        self.proposito = proposito
        self.precio = precio
        Inmueble.inmueble_list.append(self)

    @staticmethod
    def validar_nombre(nombre):
        if not isinstance(nombre, str) or nombre.isdigit():
            raise ValueError("Nombre no válido:")
        elif nombre == "":
            raise ValueError("Nombre Válido")

    @staticmethod
    def validar_proposito(proposito):
        if proposito not in ['v', 'a']:
            raise ValueError("Propósito no válido:")
        elif proposito == "":
            raise ValueError("Propósito no válido")

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
    def precio(self, nuevo_precio):
        Inmueble.validar_precio(nuevo_precio)
        self._precio = nuevo_precio


class Venta(Inmueble):
    comision_venta = 0.1
    comision_asesor = 0.03

    def __init__(self, nombre, proposito, precio, asesor):
        super().__init__(nombre, proposito, precio)
        self.comision_venta = Venta.comision_venta
        self.comision_asesor = Venta.comision_asesor
        self.asesor = asesor

    def accion_por_proposito(self):
        ganancia_asesor= self._precio*Venta.comision_asesor
        ganancia_inmobiliaria=self._precio*Venta.comision_venta

        print (f"{self.nombre} vendida exitosamente por el asesor {self.asesor}\n--La comison de {self.asesor} es de :{ganancia_asesor} \n --La comision de la inmobiliaria es:{ganancia_inmobiliaria} ")
         
 

class Alquiler(Inmueble):
    def accion_por_proposito(self):
        return f"{self.nombre} alquilada exitosamente."


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
            proposito = input("Ingrese el propósito del inmueble |venta=v| o |alquiler=a|: ")
            Inmueble.validar_proposito(proposito)
            break
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")

    while True:
        try:
            precio = float(input("Ingrese el precio del inmueble: "))
            Inmueble.validar_precio(precio)
            break
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")

    if proposito == 'v':
        asesor = input("Ingrese el nombre del asesor: ")
        inmueble = Venta(nombre, proposito, precio, asesor)
    else:
        inmueble = Alquiler(nombre, proposito, precio)

def mostrar_informcacion():
    print("\nLista de Inmuebles Registrados:")
    for inmueble in Inmueble.inmueble_list:
        print(f"--Nombre: {inmueble.nombre}|Propósito: {inmueble.proposito}|Precio: {inmueble.precio}")
    
    print(inmueble.accion_por_proposito())

mostrar_informcacion()
