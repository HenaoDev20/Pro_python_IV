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

        return f"{self.nombre} vendida exitosamente por el asesor {self.asesor}\n--La comison de {self.asesor} es de :{ganancia_asesor} \n --La comision de la inmobiliaria es:{ganancia_inmobiliaria} "

    @staticmethod
    def validar_asesor(asesor):
        if not isinstance(asesor, str) or asesor.isdigit():
            raise ValueError("Nombre no válido:")
        elif asesor == "":
            raise ValueError("Nombre Válido")
        
    @property
    def asesor(self):
        return self._asesor
    
    @asesor.setter
    def asesor(self, nuevo_asesor):
        Inmueble.validar_nombre(nuevo_asesor)
        self._asesor = nuevo_asesor


 
class Alquiler(Inmueble):
    meses = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]
    def __init__(self, nombre, proposito, precio, mes_inicio, mes_final, porcentaje):
        super().__init__(nombre, proposito, precio)
        self.mes_inicio = mes_inicio.capitalize()
        self.mes_final = mes_final.capitalize()
        self.porcentaje = porcentaje
        self.list_meses=[]
        self.calcular_meses_contrato()

    def calcular_meses_contrato(self):
        if self.mes_inicio in self.meses and self.mes_final in self.meses:
            indice_inicio = self.meses.index(self.mes_inicio)
            indice_final = self.meses.index(self.mes_final)
            if indice_final >= indice_inicio:
                self.list_meses = self.meses[indice_inicio:indice_final + 1]
            else:
                print("El mes final no puede ser anterior al mes inicial.")
        else:
            print("Mes inicial o final inválido.")

    def accion_por_proposito(self):
        return f"{self.nombre} alquilada exitosamente."

    def mostrar_detalles_contrato(self):
        if self.list_meses:
            print(f"Duración del contrato: {len(self.list_meses)} meses")
            print(f"Meses de alquiler: {', '.join(self.list_meses)}")
        else:
            print("No hay meses registrados para este contrato.")


            
    
    def accion_por_proposito(self):
        return f"{self.nombre} alquilada exitosamente."
    
while True:
    try:
        can_registros = int(input("Ingrese la cantidad de registros: "))
        if can_registros < 0:
            print("La cantidad de registros no puede ser negativa.")
        else:
            break
    except ValueError:
        print("La cantidad de registros debe ser un número válido.")


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
        while True:
            try:
                asesor = input("Ingrese el nombre del asesor: ")
                Venta.validar_asesor(asesor)
                break
            except ValueError as e:
                print(f"Error: {e}. Intente nuevamente.")

        inmueble = Venta(nombre, proposito, precio, asesor)
    elif proposito == 'a':
       while True:
            mes_inicio = input("Mes en el que desea iniciar el contrato: ").capitalize().strip()
            mes_final = input("Mes en el que desea terminar el contrato: ").capitalize().strip()

            if mes_inicio in Alquiler.meses and mes_final in Alquiler.meses:
                break
            else:
                print(f"Mes inicial '{mes_inicio}' o mes final '{mes_final}' inválido.")
                print("Los meses deben ser con la inicial en mayuscula\n")

while True:
    try:
        porcentaje = float(input("Ingrese la cantidad de porcentaje pactado con el dueño: "))
        break
    except ValueError:
        print("Porcentaje inválido. Debe ser un número.")

inmueble = Alquiler(nombre, proposito, precio, mes_inicio, mes_final, porcentaje)

       
def mostrar_informcacion():
    print("\nLista de Inmuebles Registrados:")
    for inmueble in Inmueble.inmueble_list:
        print(f"--Nombre: {inmueble.nombre}|Propósito: {inmueble.proposito}|Precio: {inmueble.precio}")
        print(inmueble.accion_por_proposito())

        if isinstance(inmueble, Alquiler):
            inmueble.mostrar_detalles_contrato()
       
    

mostrar_informcacion()
