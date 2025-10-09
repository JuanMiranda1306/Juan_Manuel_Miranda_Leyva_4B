#Practica 4       #Juan Manuel Miranda Leyva
#Crear un ticket con los siguientes tributos:
#id
#tipo(por ejemplo:software,prueba)
#prioridad(alta,media,baja)
#estado(por defecto pendiente)
#Crear dos tickets de ejemplo y mostrarlos en pantalla




class ticket:
    def __init__(self,id,tipo,prioridad):
        self.id=id
        self.tipo=tipo
        self.prioridad=prioridad
        self.estado= "pendiente" 

class empleado:
    def __init__(self,nombre):
        self.nombre=nombre
 
    def trabajar_en_ticket(self,ticket):
        print:f"El empleado {self.noombre} revisa el ticket {ticket.id}"

class desarrollador(empleado):
     def trabajar_en_ticket(self,ticket):
         if ticket.tipo=="software":
             ticket.estado=="resuelto"
             print:f"El ticket {ticket.id} fue resuelto por {self.nombre}"
         else:
             print:f"El empleado {self.nombre} no se puede hacer cargo del ticket"

class tester(empleado):
    def trabajar_en_ticket(self,ticket):
        if ticket.tipo=="prueba":
            ticket.estado=="Resuelto"
            print:f"El ticket {ticket.id} fue resuelto por {self.nombre}"
        else:
            print:f"El empleado {self.nombre} no se puede hacer cargo del ticket"

class proyect_manager(empleado):
    def asignar_ticket(self,ticket,empleado):
        print:f"{self.nombre} asigno el ticket {ticket.id},a el empleado {empleado.nombre}"
        empleado.trabajar_en_ticket(ticket)

#Crear ticket y empleados (Instancias de objetos)
ticket1=ticket(1,"software","alta")
ticket2=ticket(2,"prueba","baja")

developer1=desarrollador("jorge")
tester1=tester("Pepe")
pm=proyect_manager("Juan")

pm.asignar_ticket(ticket1,developer1)
pm.asignar_ticket(ticket2,tester1)
 
#Parte adicional
#Agregar un menu con while y con if que permita:
#Crear un ticket
#Ver tickets
#Asignar tickets
#Salir del programa

tickets = [ticket1, ticket2]

def menu():  
    ticket=0
    while True:
        print("\nAsignar los empleados de los tickets")
        print("1. Crear un ticket")
        print("2. Ver tickets")
        print("3. Asignar tickets")
        print("4. Salir")
        opcion = input("Elige una opcion:")

        if opcion == "1":
            ticket += 1            
            tickets.append({"id": ticket})
            print(f"Ticket {ticket} creado.")        
        elif opcion == "2":
            print("Tickets existentes:")
            for t in tickets:
                print(t)               
        elif opcion == "3":
            pm.asignar_ticket()
        elif opcion == "4":
            print("¡Gracias por su tiempo!")
            break  
        else:
            print("Opcion no valida. Intentalo de nuevo.")