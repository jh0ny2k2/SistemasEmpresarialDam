def menu():
    print("\n MENU DE GESTION DE FRUTERIA")
    print("1. Añadir articulo a la fruteria")
    print("2. Mostrar tienda")
    print("3. Crear nueva cesta de la compra")
    print("4. Añadir artículos a la cesta")
    print("5. Calcular total de la cesta")
    print("6. Salir")
    
def añadirArticulo(fruteria):
    nombre = input("Introduce el nombre del articulo")
    precio = float(input("Introduce el precio del articulo"))
    fruteria[nombre] = precio
    print("{nombre} añadido con un precio de {precio}")
    
def mostrarTienda(fruteria):
    print ("\n articulos en la tienda:")
    for fruta, precio in fruteria.items():
        print("\n {fruta}: {precio}")
        
def crearCesta():
    print ("Se ha creado la cesta")
    return {}
    
def añadirACesta(fruteria, cesta):
    fruta = input("Introduce el nombre de la fruta")
    if fruta in fruteria:
        cantidad = float(input("Dime la cantidad de fruta que deseas añadir"))
        precioTotal = fruteria[fruta] * cantidad
        cesta[fruta] = cesta.get(fruta, 0) + precioTotal
        print("Se han añadido {cantidad} de {fruta} con un precio de {precioTotal}")
    else: 
        print("No hay existencias de {fruta} en la fruteria")
        
def calcularTotal(cesta):
    total = sum(cesta.value())
    print ("El total de la cesta es: {total}")
    return total
    
def gestionTienda():
    fruteria = {}  # Diccionario para la frutería
    cesta = {}  # Diccionario para la cesta de la compra

    while True:
        menu()
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            añadirArticulo(fruteria)
        elif opcion == "2":
            mostrarTienda(fruteria)
        elif opcion == "3":
            cesta = crearCesta()
        elif opcion == "4":
            añadirACesta(fruteria, cesta)
        elif opcion == "5":
            calcularTotal(cesta)
        elif opcion == "6":
            print("Gracias por usar el programa de gestión de frutería. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

# Ejecutar el programa
gestionTienda()
    