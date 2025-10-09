#Practica 1 Clases, objetos y atributos
#Una clase es una plantilla o un molde que define como sera un objeto
#Miranda Leyva Juan Manuel

class Persona:
     def __init__(self,nombre,edad):           
      self.nombre= nombre
      self.edad= edad

     def presentarse(self):
        print(f"Hola mi nombre es{self.nombre}y tengo{self.edad}")
     def cumplir_anios(self):
        self.edad+=1
        print(f"Esta persona cumplio:{self.edad}años")





#Un objeto es una instancia creada a partir de una clase
#Crear objetos
estudiante1= Persona("Juan",18)
estudiante2=Persona("Miranda",19)

#Asignar metodos a esos objetos(Acciones)
estudiante1.presentarse()
estudiante1.cumplir_anios()
estudiante2.presentarse()

#Paso 1.Agrega un metodo cumplir_anios()que aumente en 1 la edad

def cumplir_anios(self):
    self.edad+=1
    print(f"Esta persona cumplio:{self.edad}años")

#Instancia: Cada objeto creado de una clase es una instacia, podemos tener varias instancias que coexistan 
#con sus propio datos.
#Objeto=instancia de la clase.
#Cada vez que se crea un o bjeto con Clase() se obtiene una instancia independiente.
#Cada instancia tiene sus propios datos aunque vengan de la misma clase.


#Abstraccion: Representar solo lo importante del mundo real ocultando detalles innecesarios  

class automovil:
    def __init__(self,marca):
        self.marca=marca
    def arrancar(self):
        print(f"{self.marca}arranco")
    
#Crear un objeto de auto y asignar una marca

auto=automovil("Toyota")
auto.arrancar()
#Abstraccion: Nos centramos solo en lo que importa(accion) 
#que es arrancar el automovil,ocultando detalles internos como motor,transmicion,tipo_combustible.
#Enfoque solo en la accion del objeto.
#El objetivo es hacer el codigo mas limpio y facil de usar.


#Practica 1.2
#1.Crear una clase mascotas
#2.Agregar minimo 4 atributos
#3.Definir al menos 4 metodos
#4.Crear 2 instancias de la clase
#5.Llamar los metodos y aplicar abstraccion.(Agregar un atributo innecesario)

class mascotas:
     def __init__(self,nombre,animal,comida,color_ojos):           
      self.nombre= nombre
      self.animal= animal
      self.comida=comida
      self.color_ojos=color_ojos

     def caracteristicas(self):
        print(f"Mi mascota se llama{self.nombre}y es un{self.animal}")
     def alimento(self):
        print(f"Mi mascota se alimenta de{self.comida}todos los dias")
     def ojos(self):
        print(f"Mi mascota tienes los ojos de color{self.color_ojos}")


mascota1= mascotas("Tito","perro","croquetas","cafes")
mascota2= mascotas("Bolita","gato","croquetas","verdes")
mascota3=mascotas("Cabo","Loro","semillas","negros")

mascota1.caracteristicas()
mascota1.alimento()
mascota1.ojos()
mascota2.caracteristicas()
mascota2.alimento()
mascota2.ojos()
mascota3.caracteristicas()
mascota3.alimento()
mascota3.ojos()
