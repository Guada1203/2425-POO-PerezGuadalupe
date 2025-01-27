#Tarea: Implementación de Constructores y Destructores en Python

"""Objetivo de la tarea:Aplicar los conceptos aprendidos sobre constructores y destructores para
desarrollar un programa en Python."""

class Zapato:
    """Clase que representa a un zapato"""

    def __init__(self, talla, modelo, color):
        """Constructor de la clase Zapato

        Args:
            talla (int): La talla del zapato
            modelo (str): El modelo del zapato
            color (str): El color del zapato
        """
        self.talla = talla
        self.modelo = modelo
        self.color = color
        print(f"El zapato modelo {self.modelo} está disponible en talla {self.talla}.")

    def probar(self):
        """Método para probar el zapato"""
        print("Me estoy probando el zapato.")

    def __del__(self):
        """Destructor de la clase Zapato"""
        print(f"El zapato {self.modelo} ha sido vendido con exito.")

# Creando un objeto de la clase Zapato
mi_zapato = Zapato(39, "Adidas", "Blanco")

# Usando el método probar
mi_zapato.probar()

# Al finalizar el bloque, se llama al destructor
print("El programa ha terminado.")
