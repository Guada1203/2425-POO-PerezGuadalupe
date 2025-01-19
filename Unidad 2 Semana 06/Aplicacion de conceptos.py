#clase base: Zapato
class Zapato:
    def __init__(self, marca, talla):
        self.marca = marca #atributos publicos
        self.talla = talla #atributos publicos

    def descripcion(self):
        return f"Zapato de marca {self.marca}, talla {self.talla}"

    def mover(self):
        return "Este zapato ya ha sido vendido."  # Mensaje más específico

#clase derivada: Zapatilla hereda de Zapato
class Zapatilla(Zapato):
    def __init__(self, marca, talla, color):
        super().__init__(marca, talla)
        self.__color = color  #atributos privados

    @property  # Decorador para acceder al atributo como si fuera una propiedad

    # metodo de acceso al atributo encapsulado
    def color(self):
        return self.__color

    # metodo sobreescrito (polimorfismo)
    def mover(self):
        return f"La zapatilla marca {self.marca}, talla {self.talla}, color {self.color} ya ha sido vendida."

#instancias y demostracion del programa

if __name__ == "__main__":
    # Creamos un zapato
    zapato = Zapato("Venus", "39")
    print(zapato.descripcion())
    print(zapato.mover())

    # Creamos una zapatilla
    zapatilla = Zapatilla(marca="Puma", talla="40", color="Blanca")
    print(zapatilla.descripcion())
    print(f"Las zapatillas son de color {zapatilla.color}")  # Acceso directo al atributo
    print(zapatilla.mover())