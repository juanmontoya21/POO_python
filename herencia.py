#HERENCIA: es cuando una superclase(clase padre) con atributros y metodos, los hereda a una subclase(clase hija)
#tipos de herencias: simple, jerarquica, multiple, multinivel.

class Persona:
    def __init__(self,Nombre, Apellido, DNI, Estatura, ColorPiel, Edad):
         self.nombre = Nombre
         self.apellido = Apellido
         self.dni = DNI
         self.estatura = Estatura
         self.color_piel = ColorPiel
         self.edad = Edad
class Docente(Persona):
     def __init__(self,Nombre, Apellido, DNI, Estatura, ColorPiel, Edad,Asignatura,Universidad,Jornada):
          super().__init__(Nombre, Apellido, DNI, Estatura, ColorPiel, Edad)
          self.asignatura = Asignatura
          self.universidad = Universidad
          self.jornada = Jornada
Docente1 = Docente("juan","vasquez","1109541148",1.70,"mestizo",19,"desarrollo","cesde","tarde")
print(Docente1.estatura)