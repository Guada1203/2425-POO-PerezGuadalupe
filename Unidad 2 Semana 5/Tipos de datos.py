
"""Objetivo de la Tarea:
Aplicar los conocimientos adquiridos sobre tipos de datos, identificadores y
 convenciones de nomenclatura en Python para desarrollar un pequeño programa.
El código será implementado en el IDE PyCharm y posteriormente publicado en el
repositorio de GitHub de cada estudiante."""

def calcular_area_triangulo(base, altura):

  """Calcula el área de un triángulo.


    base: La base del triángulo.
    altura: La altura del triángulo.

    El área del triángulo.
  """

  area = (base * altura) / 2
  return area

# Solicitar la base y la altura
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

# Calcular y mostrar el área
area = calcular_area_triangulo(base, altura)
print(f"El área del triángulo es: {area}")