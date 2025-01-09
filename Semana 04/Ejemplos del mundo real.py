class Producto:
    """Representación de un producto del supermercado"""

    def __init__(self, nombre, cantidad, valor):
        self.nombre = nombre
        self.cantidad = cantidad
        self.valor = valor

    def vender(self, cantidad_a_vender):
        if self.cantidad >= cantidad_a_vender:
            self.cantidad -= cantidad_a_vender
            print(f"se ha vendido {cantidad_a_vender} unidades de {self.nombre} ")
            return True  # Indicamos si se vendió el producto
        else:
            print(f"no hubo el producto solicitado {self.nombre} ")
            return False  # Falló la venta

class Cliente:
    """Representación del cliente"""

    def __init__(self, nombre, dinero):
        self.nombre = nombre
        self.dinero = dinero
        self.carrito = []

    def agregar_al_carrito(self, producto, cantidad):
        valor_total = producto.valor * cantidad
        if valor_total <= self.dinero:
            self.carrito.append((producto, cantidad))
            self.dinero -= valor_total  # Se resta el valor total del dinero
            print(f"{self.nombre} ha agregado {cantidad} unidades de {producto.nombre}")
        else:
            print(f"{self.nombre} no tiene suficiente dinero")

    def fin_compra(self):
        """Finaliza la compra actual del cliente, actualizando el inventario
         y calculando el total."""

        total = 0
        for producto, cantidad in self.carrito:
            if producto.vender(cantidad):
                total += producto.valor * cantidad
            else:
                print(f"No se pudo vender {cantidad} unidades de {producto.nombre}")

        print(f"{self.nombre} ha finalizado su compra. Total: {total}")
        self.carrito = []  # Vaciar el carrito

# Creación de objetos
galletas = Producto("Galletas", 10, 0.75)
helados = Producto("Helados", 5, 0.50)

cliente = Cliente("Luis", 10)

# Interacciones
cliente.agregar_al_carrito(galletas, 10)
cliente.agregar_al_carrito(helados, 5)
cliente.fin_compra()
