def menu():
    print("\n MENU DE GESTION DE FRUTERIA")
    print("1. Añadir palabras al Diccionario")
    print("2. Traducir")
    print("3. Salir")
    
def addPalabra(diccionario):
    entrada = input("Introduce palabras en formato <español>:<inglés> separadas por comas: ")
    pares = entrada.split(',')

    for par in pares:
        try:
            español, ingles = par.split(':')
            diccionario[español.strip()] = ingles.strip()
        except ValueError:
            print(f"Formato incorrecto en: '{par}'. Debe ser <español>:<inglés>.")
    
    print("Palabra añadida correctamente.")

def traducir(diccionario):
    frase = input("Dime la palabra que quieres traducir")
    palabras = frase.split()
    traduccion = []
    
    for palabra in palabras:
        traduccion.append(diccionario.get(palabra, palabra))
        
    fraseTraducida = " ".join(traduccion)
    print (fraseTraducida)
    
    
def diccionario():
    diccionario = {}

    while True:
        menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            addPalabra(diccionario)
        elif opcion == "2":
            traducir(diccionario)
        elif opcion == "3":
            print("Gracias por usar el programa de gestión de frutería. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

# Ejecutar el programa
diccionario()