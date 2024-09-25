
def binario_a_decimal(binario):
    # Convertimos la cadena binaria en un número decimal
    return int(binario, 2)

# Ejemplo de uso:
binario = "1010"
decimal = binario_a_decimal(binario)
print(f"Binario {binario} a decimal es: {decimal}")

def decimal_a_binario(decimal):
    # Convertimos el número decimal en una cadena binaria
    return bin(decimal)[2:]

# Ejemplo de uso:
decimal = 10
binario = decimal_a_binario(decimal)
print(f"Decimal {decimal} a binario es: {binario}")