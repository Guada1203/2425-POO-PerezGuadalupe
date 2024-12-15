#usando el codigo POO
class DiaClima:
    def __init__(self, temperatura):
        self.__temperatura = temperatura

    def get_temperatura(self):
        return self.__temperatura

    def set_temperatura(self, temperatura):
        self.__temperatura = temperatura

class SemanaClima:
    def __init__(self):
        self.dias = []

    def agregar_dia(self, dia):
        self.dias.append(dia)

    def calcular_promedio_semanal(self):
        temperaturas = [dia.get_temperatura() for dia in self.dias]
        return sum(temperaturas) / len(temperaturas)

# Bloque principal del programa
semana = SemanaClima()
for _ in range(8):
    temperatura = float(input("Ingrese la temperatura del día: "))
    dia = DiaClima(temperatura)
    semana.agregar_dia(dia)

promedio_semanal = semana.calcular_promedio_semanal()
print("El promedio semanal de temperaturas es:", promedio_semanal)