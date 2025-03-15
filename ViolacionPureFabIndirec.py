class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_pedido(self, cocinero, platos):
        cocinero.preparar_plato(platos)

class Cocinero:
    def preparar_plato(self, platos):
        print(f"Cocinero preparando: {', '.join(platos)}")

class Pedido:
    def __init__(self, cliente, platos):
        self.cliente = cliente
        self.platos = platos

    def calcular_total(self, impuesto=0.1, propina=0.15):  # ❌ Lógica mal ubicada
        subtotal = sum(plato['precio'] for plato in self.platos)
        return subtotal + (subtotal * impuesto) + (subtotal * propina)

# Uso del sistema
cliente = Cliente("Juan")
cocinero = Cocinero()
platos = [{"nombre": "Pizza", "precio": 10}, {"nombre": "Pasta", "precio": 12}]

cliente.hacer_pedido(cocinero, platos)  # ❌ Cliente depende directamente del cocinero
pedido = Pedido(cliente, platos)
total = pedido.calcular_total()  # ❌ La clase Pedido tiene lógica extra

print(f"Total a pagar: ${total:.2f}")

❌ Se viola Indirection → Cliente habla directamente con Cocinero, lo que hace el código poco flexible.
    
❌ Se viola Pure Fabrication → Pedido tiene la lógica de cálculo de cuentas, lo que rompe el SRP (Single Responsibility Principle).
