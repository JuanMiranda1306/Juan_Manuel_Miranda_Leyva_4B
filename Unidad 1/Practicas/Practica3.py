#Practica 3. Introduccion al polimorfismo
#Simular un sitema de cobro con multiples opciones de pago

class pago_tarjeta:
    def procesar_pago(self,cantidad)
    return f"Procesando pago de ${cantidad} con tarjeta"
    

class transferencia:
    def procesar_pago(self,cantidad)
    return f"Procesando pago con transferencia por la cantidad de ${cantidad}"

class deposito:
    def procesar_pago(self,cantidad)
    return f"Procesando pago por deposito por la cantidad de ${cantidad}"

class paypal:
    def procesar_pago(self,cantidad)
    return f"Procesando pago con paypal por la cantidad de ${cantidad}"

#Instancia
metodos_pago=[pago_tarjeta(),transferencia(),deposito(),paypal()]

for m in metodos_pago:
    print(m.procesar_pago(500))



#Actividad: Procesar pago con diferentes cantidades en cada uno de las formas de pago, ejemplo:
#100 con tarjeta, 500 con transferencia, 2000 con paypal, 400 con deposito

pago1=pago_tarjeta()
pago2=transferencia()
pago3=paypal()
pago4=deposito()

print(pago1.procesar_pago(100))
print(pago2.procesar_pago(500))
print(pago3.procesar_pago(2000))
print(pago4.procesar_pago(400))




#Ejemplo 2
#Notificaciones de mensajes

class mensajes:
    def notificacion(self,mensaje)
    return f"Has recibido un {mensaje} de la aplicacion mensajes"

class gmail:
    def notificacion(self,mensaje)
    return f"Has recibido un {mensaje} de la aplicacion gmail"
        
class whastsapp:
    def notificacion(self,mensaje)
    return f"Has recibido un {mensaje} de la aplicacion whastsapp"

class instagram:
    def notificacion(self,mensaje)
    return f"Has recibido un {mensaje} de la aplicacion instagram"

class facebook:
    def notificacion(self,mensaje)
    return f"Has recibido un {mensaje} de la aplicacion facebook"

class tinder:
    def notificacion(self,mensaje)
    return f"Has recibido un {mensaje} de la aplicacion tinder"

class telegram:
    def notificacion(self,mensaje)
    return f"Has recibido un {mensaje} de la aplicacion telegram"

tipo_notificacion=[mensajes(),gmail(),whastsapp(),instagram(),facebook(),tider(),telegram]

for m in tipo_notificacion:
    print(m.notificacion)







def identificador(self):
    print:f"Tu id es {self.identificador}"
def software(self):
    print:f"El {self.software} fue el comprado" 
def alta (self):
    print:f"La gama del  dispositivo es {self.alta}"
def pendiente(self):
    print:f"Su estado es {self.pendiente}"