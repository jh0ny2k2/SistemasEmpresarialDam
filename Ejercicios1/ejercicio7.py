def collatz_recorrido(n, memorizacion):
    # Si ya hemos calculado el recorrido para n, simplemente lo devolvemos
    if n in memorizacion:
        return memorizacion[n]
    
    # Caso base: si n es 1, el recorrido es solo [1]
    if n == 1:
        memorizacion[n] = [1]
        return [1]
    
    # Si n es par, dividimos por 2; si es impar, multiplicamos por 3 y sumamos 1
    if n % 2 == 0:
        siguiente = n // 2
    else:
        siguiente = 3 * n + 1
    
    # Calculamos el recorrido para el siguiente número y lo guardamos
    recorrido = [n] + collatz_recorrido(siguiente, memorizacion)
    memorizacion[n] = recorrido
    return recorrido

def calcular_collatz_hasta_100():
    memorizacion = {}  # Diccionario para guardar los recorridos ya calculados
    recorridos = []    # Lista para guardar los recorridos de cada número

    # Calculamos el recorrido para cada número del 1 al 100
    for i in range(1, 101):
        recorrido = collatz_recorrido(i, memorizacion)
        recorridos.append(recorrido)

    # Encontrar el número con el recorrido más largo
    numero_con_mas_largo_recorrido = max(recorridos, key=len)

    return recorridos, numero_con_mas_largo_recorrido

# Ejecución
recorridos, recorrido_mas_largo = calcular_collatz_hasta_100()

# Mostrar resultados
for i, recorrido in enumerate(recorridos, start=1):
    print(f"Número {i}: Recorrido {recorrido}")

print("\nEl número con el recorrido más largo es:", recorrido_mas_largo[0])
print("Su recorrido es:", recorrido_mas_largo)
