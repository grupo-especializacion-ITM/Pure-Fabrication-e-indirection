class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_pedido(self, mesero, platos):
        mesero.tomar_pedido(self, platos)

class Cocinero:
    def preparar_plato(self, pedido):
        print(f"Cocinero preparando: {', '.join(pedido.platos)}")


 "Aplicamos Indirection (Capa Intermedia: Mesero)"
class Mesero:
    def __init__(self):
        self.cocinero = Cocinero()

    def tomar_pedido(self, cliente, platos):
        pedido = Pedido(cliente, platos)
        self.cocinero.preparar_plato(pedido)

"Aplicamos Pure Fabrication (Clase que no existe en la vida real)"
class Pedido:
    def __init__(self, cliente, platos):
        self.cliente = cliente
        self.platos = platos

class CalculadorDeCuenta:  # PURE FABRICATION
    @staticmethod
    def calcular_total(pedido, impuesto=0.1, propina=0.15):
        subtotal = sum(plato['precio'] for plato in pedido.platos)
        total = subtotal + (subtotal * impuesto) + (subtotal * propina)
        return total
