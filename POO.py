#PROGRAMACION ORIENTADA A OBJETOS:paradigma(moselo de estructura) que imita objetos reales (atributros y funcionalidad).
#4 principios: herencia, encapsulamiento, abstracion y el polimorfismo.

#objeto: conjunto de atributros(propiedades o caracteristicas) y metodos(funcionalidad).
#ejemplo: 

""""
OBJETO: vehiculo
atributos: color, tipo, capacidad, modelo,marca,precio
metodos: frenar, acelerar, direccion, reversar, girar, encender, apagar.
"""

#CLASE: estructura que contiene los atributros y metodos de objeto


"""class Vehiculo: #creando clase
    Color = "verde"
    Tipo = "estandar"
    capacidad = 5
    Modelo = 96
    marca = "BMW"
    precio = 8000000"""

#instanciar objeto: crear el objeto
# vehiculo = Vehiculo()

# print(vehiculo.Tipo)

class Vehiculo:
    def __init__(self, Color, Tipo, Capacidad, Modelo, Marca, Precio) :
        self.color = Color
        self.tipo = Tipo
        self.capacidad = Capacidad
        self.modelo = Modelo
        self.marca = Marca
        self.precio = Precio
        
    def Inforvehiculo(self):
        print(f"las caracteriticas de vehiculo son \ncolor:{self.color}\ntipo:{self.tipo}\ncapacidad:{self.capacidad}\nmodelo:{self.modelo}\nmarca:{self.marca}\nprecio:{self.precio}")
    def direccion(self,avanzar,girar):
        if avanzar == True:
            print(f"el carro esta avanzando:{avanzar},esta girando a la {girar}")
        else:
            print("el vehiculo esta apagado")

vehiculo1 = Vehiculo("verde","estandar",5,96,"BMW",8000000)
vehiculo2 = Vehiculo("Amarillo","Taxi",5,2023,"KIA",44500000)


# print(vehiculo1.color)
# vehiculo2.Inforvehiculo()
vehiculo1.direccion(True,"derecha")

#cambiar el valor a un atributro
# vehiculo2.marca = "perro"
# print(vehiculo2.marca)


#