#Tarea: Sistema Avanzado de Gestión de Inventario.

"""Desarrollar un sistema avanzado de gestión de inventarios para una tienda,
 que incorpore las colecciones en POO para un
 manejo eficiente de los ítems del inventario y almacene la información del inventario en archivos."""

"""Objetivos:
Aplicar los conceptos de POO para la estructura del programa.
Utilizar colecciones (listas, diccionarios, conjuntos, tuplas) para gestionar los datos del inventario.
Implementar la lectura y escritura de archivos para el almacenamiento persistente del inventario."""

import json

class Libro:
    def __init__(self, id, titulo, autor, cantidad, precio):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Título: {self.titulo}, Autor: {self.autor}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Libreria:
    def __init__(self):
        self.libros = {}

    def agregar_libro(self, libro):
        self.libros[libro.id] = libro

    def eliminar_libro(self, id):
        if id in self.libros:
            del self.libros[id]

    def actualizar_libro(self, id, cantidad=None, precio=None):
        if id in self.libros:
            if cantidad is not None:
                self.libros[id].cantidad = cantidad
            if precio is not None:
                self.libros[id].precio = precio

    def buscar_libro_por_titulo(self, titulo):
        resultados = [libro for libro in self.libros.values() if titulo.lower() in libro.titulo.lower()]
        for libro in resultados:
            print(libro)

    def mostrar_inventario(self):
        for libro in self.libros.values():
            print(libro)

    def guardar_inventario(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'w') as file:
                json.dump({id: libro.__dict__ for id, libro in self.libros.items()}, file, indent=4)
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_inventario(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as file:
                data = json.load(file)
            for id, libro_data in data.items():
                self.libros[id] = Libro(**libro_data)
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON. El archivo podría estar corrupto.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

def mostrar_menu():
    print("\n--- Gestión de Librería ---")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Actualizar libro")
    print("4. Buscar libro por título")
    print("5. Mostrar inventario")
    print("6. Guardar y salir")
    print("7. Salir sin guardar")

def main():
    libreria = Libreria()
    libreria.cargar_inventario("libreria.json")

    libro1 = Libro("001", "El Señor de los Anillos", "J.R.R. Tolkien", 5, 30.00)
    libro2 = Libro("002", "Orgullo y prejuicio", "Jane Austen", 8, 25.00)
    libro3 = Libro("003", "Don Quijote de la Mancha", "Miguel de Cervantes", 3, 35.00)
    libreria.agregar_libro(libro1)
    libreria.agregar_libro(libro2)
    libreria.agregar_libro(libro3)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id = input("ID: ")
                titulo = input("Título: ")
                autor = input("Autor: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                libro = Libro(id, titulo, autor, cantidad, precio)
                libreria.agregar_libro(libro)
                print("Libro agregado.")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio.")
            except Exception as e:
                print(f"Error inesperado: {e}")

        elif opcion == "2":
            id = input("ID del libro a eliminar: ")
            libreria.eliminar_libro(id)
            print("Libro eliminado.")

        elif opcion == "3":
            id = input("ID del libro a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            try:
                if cantidad:
                    cantidad = int(cantidad)
                if precio:
                    precio = float(precio)
                libreria.actualizar_libro(id, cantidad=cantidad, precio=precio)
                print("Libro actualizado.")
            except ValueError:
                print("Error: Ingrese valores numéricos válidos para cantidad y precio.")
            except Exception as e:
                print(f"Error inesperado: {e}")

        elif opcion == "4":
            titulo = input("Título a buscar: ")
            libreria.buscar_libro_por_titulo(titulo)

        elif opcion == "5":
            libreria.mostrar_inventario()

        elif opcion == "6":
            libreria.guardar_inventario("libreria.json")
            print("Inventario guardado. ¡Hasta luego!")
            break

        elif opcion == "7":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()