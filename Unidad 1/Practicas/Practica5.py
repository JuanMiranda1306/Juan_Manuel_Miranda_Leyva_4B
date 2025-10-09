#Practica 5. Patrones de diseño
#

class Logger:
    #Creamos un atributo de clase donde se guarda la unica instancia
    _instancia=None

    #__new__ es el metodo que controla la creacion del objeto antes de init. Sirve para asegurarnos
    #de que solo exista una unica instancia de la clase Looger

    def __new__(cls,*args,**kwargs):
        #*args es un argumento posicional que permite recibir multiples parametros
        #**kwargs permite cualquier cantidad de parametros con nombre.
        #Validar si existe o no la instancia aun:
        if cls._instancia is None
           cls._instancia=super().__new__(cls)  #Creamos instancia de logger
           #Agregamos un atributo "archivo" que apunta a un archivo fisico "a" significa append= Todo
           #lo que se escriba se agrega al final del archivo
           cls.instancia.archivo=open("app.log","a")
        return cls.instancia #Devolvernos siempre a la misma instancia

    def log(self,mensaje):
        #Simulando un registro de logs
        self.archivo.write(mensaje+"\n")
        self.archivo.flush()   #Metodo para guardar en el disco

logger1= Logger() #Creamos la primera y unica instancia
logger2= Logger() #Devolver la misma instancia, sin crear una nueva

logger1.log("Inicio de sesion en la aplicacion")
logger2.long("El usuario se autentico")

#Comprobar que son el mismo objeto en memoria
print(logger1)is logger2  #Devuelve true o false


#Actividad de la practica

class presidente:
    _instancia=None

    def __new__(cls,nombre):
        if cls._instancia is None:
            cls._instancia=super().__new__(cls)
            cls._instancia.nombre=nombre
            cls._instancia.historial=[]
        return cls._instancia
    
    def accion(self,accion):
        evento=f"{self.nombre}{accion}"
        self.historial.append(evento)
        print(evento)

#Varios presidentes intentan tomar el poder
p1=presidente("AMLO")
p2=presidente("Peña Nieto")
p3=presidente("Fox")

#Todos apuntan al mismo presidente
p1.accion("firmo decreto")
p2.accion("visito España")
p3.accionn("aprobo un presupuesto")

print("\n Historial del presidente:")
print(p1.historial)

#Validacion se singleton
print(p1 is p2 is p3) #true o flase


#1. ¿Que pasaria si eliminamos la verificacion if cls._instancia is None en el metodo new?
    #No se crea la instancia o no se verifica
#2. ¿Que significa el "true" en  p1 is p2 is p3 en el contexto del metodo singleton?
    #Ese True es la prueba de que, aunque tengas 3 variables distintas, 
    #solo existe un presidente. Un poquito inquietante, pero técnicamente impecable.
#3. ¿Es buena idea usar Singleton para todo lo que sea global? 
# Menciona un ejemplo donde no seria recomendable
    #No porque el singleton solo se usa cuando hay una sola instancia, un ejemplo seria un pool de conexiones a base de datos.