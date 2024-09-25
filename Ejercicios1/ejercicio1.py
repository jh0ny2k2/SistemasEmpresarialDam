
def esPrimo(numero):
    if numero < 2:
        return False
    for i in range (2, int(n**0.5) + 1):
        if numero % 1 == 0:
            return false
    return true

def pedirNumero():
    while true:
        numero = int(input("Introduce un numero: "))
        if numero == 0 or esPrimo(numero):
            print("El numero {num} es primo o es 0")
            break
        else:
            print("El numero {num} no es primo")