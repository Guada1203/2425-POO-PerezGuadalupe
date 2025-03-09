"""Objetivo: Desarrollar un sistema para gestionar una biblioteca digital. El sistema permitirá administrar
los libros disponibles, las categorías de libros, los usuarios registrados y el historial de préstamos."""
import json

class Libro:
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.prestado = prestado

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "prestado": self.prestado
        }

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        else:
            print(f"{self.nombre} no tiene prestado el libro {libro}.")

class Biblioteca:
    def __init__(self, archivo_json='biblioteca.json'):
        self.archivo_json = archivo_json
        self.libros = self.cargar_libros()
        self.usuarios = []  # Añadimos una lista para almacenar usuarios

    def cargar_libros(self):
        try:
            with open(self.archivo_json, 'r') as archivo:
                datos_libros = json.load(archivo)
                return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
        except FileNotFoundError:
            # Añadir libros iniciales desde la tupla
            libros_iniciales = (
                ("Cien años de soledad", "Gabriel García Márquez", "001A", "Novela"),
                ("1984", "George Orwell", "002B", "Ciencia ficción"),
                ("El señor de los anillos", "J.R.R. Tolkien", "003C", "Fantasía"),
                ("Orgullo y prejuicio", "Jane Austen", "004D", "Romance"),
                ("Don Quijote de la Mancha", "Miguel de Cervantes", "005E", "Clásico"),
            )
            libros = {}
            for titulo, autor, isbn, categoria in libros_iniciales:
                libro = Libro(isbn, titulo, autor, categoria)
                libros[isbn] = libro
            return libros

    def guardar_libros(self):
        with open(self.archivo_json, 'w') as archivo:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4)

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        self.guardar_libros()

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            self.guardar_libros()
            print(f"Libro {isbn} eliminado con éxito.")
        else:
            print(f"No se encontró ningún libro con ISBN {isbn}.")

    def prestar_libro(self, isbn, usuario):
        libro = self.libros.get(isbn)
        if libro:
            if not libro.prestado:
                libro.prestado = True
                usuario.prestar_libro(libro)
                self.guardar_libros()
                print(f"Libro {isbn} prestado con éxito a {usuario.nombre}.")
            else:
                print("Libro no disponible para préstamo.")
        else:
            print("Libro no encontrado.")

    def devolver_libro(self, isbn, usuario):
        libro = self.libros.get(isbn)
        if libro and libro.prestado:
            libro.prestado = False
            usuario.devolver_libro(libro)
            self.guardar_libros()
            print(f"Libro {isbn} devuelto con éxito por {usuario.nombre}.")
        else:
            print("Error en la devolución del libro.")

    def buscar_libros(self):
        termino = input("Ingrese el título, autor o ISBN a buscar: ").lower()
        resultados = []
        for libro in self.libros.values():
            if termino in libro.titulo.lower() or termino in libro.autor.lower() or termino in libro.isbn.lower():
                resultados.append(libro)
        if resultados:
            print("Resultados de la búsqueda:")
            for libro in resultados:
                print(f"ISBN: {libro.isbn}, Título: {libro.titulo}, Autor: {libro.autor}, Categoría: {libro.categoria}, Prestado: {'Sí' if libro.prestado else 'No'}")
        else:
            print("No se encontraron libros que coincidan con la búsqueda.")

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Usuario {usuario.nombre} agregado con éxito.")

    def dar_de_baja_usuario(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                self.usuarios.remove(usuario)
                print(f"Usuario {usuario.nombre} eliminado con éxito.")
                return
        print(f"No se encontró ningún usuario con ID {id_usuario}.")

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Añadir Libro\n2. Buscar Libros\n3. Agregar usuario\n4. Dar de baja usuario\n5. Prestar Libro\n6. Devolver Libro\n7. Quitar Libro\n8. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            libro = Libro(isbn, titulo, autor, categoria)
            biblioteca.añadir_libro(libro)
        elif opcion == '2':
            biblioteca.buscar_libros()
        elif opcion == '3':
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.agregar_usuario(usuario)
        elif opcion == '4':
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_de_baja_usuario(id_usuario)
        elif opcion == '5':
            isbn = input("ISBN del libro a prestar: ")
            id_usuario = input("ID del usuario que presta el libro: ")
            usuario = None
            for u in biblioteca.usuarios:
                if u.id_usuario == id_usuario:
                    usuario = u
                    break
            if usuario:
                biblioteca.prestar_libro(isbn, usuario)
            else:
                print("Usuario no encontrado.")
        elif opcion == '6':
            isbn = input("ISBN del libro a devolver: ")
            id_usuario = input("ID del usuario que devuelve el libro: ")
            usuario = None
            for u in biblioteca.usuarios:
                if u.id_usuario == id_usuario:
                    usuario = u
                    break
            if usuario:
                biblioteca.devolver_libro(isbn, usuario)
            else:
                print("Usuario no encontrado.")
        elif opcion == '7':
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)
        elif opcion == '8':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()