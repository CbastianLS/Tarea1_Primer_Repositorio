import string
import random

# Letras y números disponibles
minusculas_ascii = string.ascii_lowercase
print(minusculas_ascii)

mayusculas_ascii = string.ascii_uppercase
print(mayusculas_ascii)

numeros = string.digits
print(numeros)

def generarPassword(n):
    # Verificamos que la longitud sea suficiente para incluir al menos un carácter de cada tipo
    if n < 3:
        raise ValueError("La longitud mínima para el password debe ser 3")

    # Seleccionamos al menos una letra minúscula, una mayúscula y un número
    password = [
        random.choice(minusculas_ascii),
        random.choice(mayusculas_ascii),
        random.choice(numeros)
    ]

    # Rellenamos el resto de caracteres al azar, tomando de las tres listas combinadas
    caracteres = minusculas_ascii + mayusculas_ascii + numeros
    password += random.choices(caracteres, k=n - 3)

    # Mezclamos los caracteres para que no sigan un patrón
    random.shuffle(password)

    # Convertimos la lista de caracteres en una cadena
    return ''.join(password)

# Generamos passwords de diferentes longitudes (10 a 19 caracteres)
for i in range(10, 20):
    print(generarPassword(i))
