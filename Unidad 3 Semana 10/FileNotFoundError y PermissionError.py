def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return None
    except PermissionError:
        print(f"Error: No tienes permisos para leer el archivo '{nombre_archivo}'.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None

# Ejemplo de uso
contenido = leer_archivo("mi_archivo.txt")
if contenido:
    print(contenido)

def escribir_archivo(nombre_archivo, texto):
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(texto)
    except PermissionError:
        print(f"Error: No tienes permisos para escribir en el archivo '{nombre_archivo}'.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejemplo de uso
escribir_archivo("mi_archivo.txt", "Este es un ejemplo de texto.")