import math

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")

        self.signo = -1 if (numerador < 0) ^ (denominador < 0) else 1
        
        numerador = abs(numerador)
        denominador = abs(denominador)
        
        gcd = math.gcd(numerador, denominador)
        self.numerador = numerador // gcd
        self.denominador = denominador // gcd

    def __str__(self):
        signo_str = '-' if self.signo == -1 else ''
        return f"{signo_str}{self.numerador}/{self.denominador}"

    def sumar(self, otra):

        nuevo_denominador = self.denominador * otra.denominador
        nuevo_numerador = (self.signo * self.numerador * otra.denominador) + (otra.signo * otra.numerador * self.denominador)


        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __eq__(self, otra):
        
        return self.signo * self.numerador * otra.denominador == otra.signo * otra.numerador * self.denominador
    
    def __lt__(self, otra):
        
        return self.signo * self.numerador * otra.denominador < otra.signo * otra.numerador * self.denominador

    def __le__(self, otra):
        
        return self.__eq__(otra) or self.__lt__(otra)

# Ejemplos de uso:

# Crear dos fracciones
fraccion1 = Fraccion(8, 45)
fraccion2 = Fraccion(-9, 25)

# Mostrar las fracciones
print(f"Fracción 1: {fraccion1}") 
print(f"Fracción 2: {fraccion2}")  

# Sumar fracciones
resultado_suma = fraccion1.sumar(fraccion2)
print(f"Suma: {resultado_suma}")  

# Comparar fracciones
print(f"Fracción 1 es igual a Fracción 2: {fraccion1 == fraccion2}")  
print(f"Fracción 1 es menor que Fracción 2: {fraccion1 < fraccion2}")
        