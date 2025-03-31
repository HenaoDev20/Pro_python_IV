class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_informacion(self):  
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}")


class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Cantidad de puertas: {self.numero_puertas}")


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, cilindraje):
        super().__init__(marca, modelo, año)
        self.cilindraje = cilindraje
      
    def mostrar_informacion(self): 
        super().mostrar_informacion() 
        print(f"Cilindraje: {self.cilindraje}")



auto = Automovil("Toyota", "Corolla", 2022, 4)
moto = Motocicleta("Yamaha", "YBR", 2020, 150)


auto.mostrar_informacion()
print()  
moto.mostrar_informacion()
