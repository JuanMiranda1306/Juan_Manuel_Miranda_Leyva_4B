
# Ejemplo práctico: Cafetería con Factory y Observer


# ----------- FACTORY -----------
# La Fábrica se encarga de crear distintos tipos de bebidas

class Bebida:
    """Clase base para cualquier bebida"""
    def __init__(self, nombre):
        self.nombre = nombre

    def preparar(self):
        raise NotImplementedError("Debes implementar este método en la subclase")


class Cafe(Bebida):
    def __init__(self):
        super().__init__("Café")

    def preparar(self):
        return "Moliendo granos y preparando café espresso."


class Te(Bebida):
    def __init__(self):
        super().__init__("Té")

    def preparar(self):
        return "Infusionando hojas de té con agua caliente."


class Chocolate(Bebida):
    def __init__(self):
        super().__init__("Chocolate")

    def preparar(self):
        return "Mezclando cacao en polvo con leche caliente."


class BebidaFactory:
    """Fábrica que crea bebidas sin necesidad de exponer la lógica al cliente"""
    @staticmethod
    def crear_bebida(tipo):
        if tipo == "cafe":
            return Cafe()
        elif tipo == "te":
            return Te()
        elif tipo == "chocolate":
            return Chocolate()
        else:
            raise ValueError("No tenemos esa bebida en el menú.")


# ----------- OBSERVER -----------
# Los clientes esperan notificación cuando su pedido esté listo.

class Observer:
    """Interfaz para los observadores"""
    def actualizar(self, mensaje):
        pass


class Cliente(Observer):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"Notificación para {self.nombre}: {mensaje}")


class Cafeteria:
    """Sujeto observado: la cafetería"""
    def __init__(self):
        self.observadores = []

    def agregar_cliente(self, cliente):
        self.observadores.append(cliente)

    def quitar_cliente(self, cliente):
        self.observadores.remove(cliente)

    def notificar(self, mensaje):
        for cliente in self.observadores:
            cliente.actualizar(mensaje)

    def preparar_pedido(self, tipo_bebida):
        bebida = BebidaFactory.crear_bebida(tipo_bebida)
        proceso = bebida.preparar()
        self.notificar(f"Tu {bebida.nombre} está listo. {proceso}")


# ----------- DEMOSTRACIÓN -----------
if __name__ == "__main__":
    # Creamos la cafetería (sujeto observado)
    cafeteria = Cafeteria()

    # Registramos clientes como observadores
    cliente1 = Cliente("Ana")
    cliente2 = Cliente("Luis")
    cafeteria.agregar_cliente(cliente1)
    cafeteria.agregar_cliente(cliente2)

    # Se preparan bebidas (la fábrica crea y el observer notifica)
    cafeteria.preparar_pedido("cafe")
    cafeteria.preparar_pedido("te")

    # Luis se va antes de su chocolate
    cafeteria.quitar_cliente(cliente2)
    cafeteria.preparar_pedido("chocolate")
