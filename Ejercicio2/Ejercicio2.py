import math

class FiguraGeometrica:
    
    def superficie(self):
        return 0
    

class TrianguloRectangulo:
    
    def __init__(self, cateto1, cateto2):
        self.cateto1 = cateto1
        self.cateto2 = cateto2
        
    def hipotenusa(self):
        
        return math.sqrt(self.cateto1 ** 2 + self.cateto2 ** 2)
    
    def superficie(self):
        
        return (self.cateto1 * self.cateto2) / 2
    

class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def superficie(self):
        
        return self.base * self.altura
    
class ListaFiguras:
    
    def __init__(self):
        self.figuras = []
        
    def añadirTriangulo(self, cateto1, cateto2):
        triangulo = TrianguloRectangulo(cateto1, cateto2)
        self.figuras.append(triangulo)
        
    def añadirRectangulo(self, base, altura):
        rectangulo = Rectangulo(base, altura)
        self.figuras.append(rectangulo)
        
    def superficieTotal(self):
        return sum(figura.superficie() for figura in self.figuras)
    
    def contarTriangulos(self):
        return sum(1 for figura in self.figuras if isinstance(figura, TrianguloRectangulo))
    
    

listaFiguras = ListaFiguras()

listaFiguras.añadirRectangulo(5, 9)
listaFiguras.añadirTriangulo(12,6)
listaFiguras.añadirRectangulo(3, 4)

print(f"Superficie total: {listaFiguras.superficieTotal()}")
print(f"Total de triángulos: {listaFiguras.contarTriangulos()}")