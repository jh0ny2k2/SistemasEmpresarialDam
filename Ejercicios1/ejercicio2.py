def division_controlada(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        return 0
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return 0
    return resultado

# Ejemplo de uso:
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
print("Resultado de la división:", division_controlada(a, b))