def longitudes (lista1, lista2):
    
    if len(lista1) == len(lista2):
        print("Las listas deben tener la misma longitud.")
        
        return list(map(lambda x, y: max(x, y), lista1, lista2))
        
lista1 = [3,2,5]
lista2 = [4,1,1]

resultado = longitudes(lista1, lista2)
print (resultado)