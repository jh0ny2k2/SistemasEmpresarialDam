def inversa(cadena):
    lista = list(cadena)
    
    lista.reverse();
    
    return ''.join(lista)
    
cadena = "Hola Mundo"
print(inversa(cadena))