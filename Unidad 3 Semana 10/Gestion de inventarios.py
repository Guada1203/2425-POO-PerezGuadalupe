import random

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_inventario()

    def generar_codigo(self, nombre):
        """Genera un código único para cada producto."""
        return f"{nombre[:3].upper()}-{random.randint(100, 999)}"

    def agregar_producto(self, nombre, cantidad, precio):
        codigo = self.generar_codigo(nombre)
        self.productos[codigo] = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
        self.guardar_inventario()
        print(f"Producto '{nombre}' (Código: {codigo}) agregado con éxito.")

    def actualizar_producto(self, codigo, cantidad=None, precio=None):
        if codigo in self.productos:
            if cantidad is not None:
                self.productos[codigo]["cantidad"] = cantidad
            if precio is not None:
                self.productos[codigo]["precio"] = precio
            self.guardar_inventario()
            print(f"Producto con código '{codigo}' actualizado con éxito.")
        else:
            print(f"Error: Producto con código '{codigo}' no encontrado.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_inventario()
            print(f"Producto con código '{codigo}' eliminado con éxito.")
        else:
            print(f"Error: Producto con código '{codigo}' no encontrado.")

    def cargar_inventario(self):
        try:
            with open(self.archivo, "r") as archivo:
                for linea in archivo:
                    codigo, nombre, cantidad, precio = linea.strip().split(",")
                    self.productos[codigo] = {"nombre": nombre, "cantidad": int(cantidad), "precio": float(precio)}
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
            self.guardar_inventario()  # Crea el archivo vacío
        except PermissionError:
            print(f"Error: No tienes permisos para leer '{self.archivo}'.")
        except ValueError:
            print("Error: El archivo de inventario está defectuoso. Se utilizará un inventario vacío.")
            self.productos = {}

    def guardar_inventario(self):
        try:
            with open(self.archivo, "w") as archivo:
                for codigo, datos in self.productos.items():
                    archivo.write(f"{codigo},{datos['nombre']},{datos['cantidad']},{datos['precio']}\n")
        except PermissionError:
            print(f"Error: No tienes permisos para escribir en '{self.archivo}'.")

def mostrar_menu():
    print("\n--- Gestión de Inventario ---")
    print("1. Agregar producto")
    print("2. Actualizar producto")
    print("3. Eliminar producto")
    print("4. Mostrar inventario")
    print("5. Salir")

def main():
    inventario = Inventario()

    # Agregar productos de ejemplo al inicio
    inventario.agregar_producto("Leche", 10, 1.50)
    inventario.agregar_producto("Queso", 15, 2.50)
    inventario.agregar_producto("Mantequilla", 30, 3.75)
    inventario.agregar_producto("Pan", 90, 1.25)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == "2":
            codigo = input("Código del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(codigo, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == "3":
            codigo = input("Código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)
        elif opcion == "4":
            print("\nInventario actual:")
            for codigo, datos in inventario.productos.items():
                print(f"- {codigo}: {datos['nombre']}, Cantidad={datos['cantidad']}, Precio={datos['precio']}")
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()