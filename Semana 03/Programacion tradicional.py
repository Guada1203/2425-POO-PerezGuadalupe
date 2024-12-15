#Promedio semanal del clima
#funcion para el ingreso de temperaturas

def ingresar_temperaturas_semanales():
    """
    Ingresa las temperaturas diarias de una semana y las almacena en una lista.
    """
    temperaturas = []
    for dia in range(1, 8):
        temperatura = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temperatura)
    return temperaturas

#funciones para calular el promedio

def calcular_promedio(temperaturas):
    """
    Calcula el promedio de una lista de temperaturas.
    """
    suma_temperaturas = sum(temperaturas)
    promedio = suma_temperaturas / len(temperaturas)
    return promedio

# Bloque principal del programa
temperaturas_semana = ingresar_temperaturas_semanales()
promedio_semanal = calcular_promedio(temperaturas_semana)

#imprimimos el promedio semanal de temperaturas

print("El promedio semanal de temperaturas es:", promedio_semanal)