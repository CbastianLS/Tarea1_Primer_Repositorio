import random

# Inicializamos las listas
lista_pares = [] 
lista_impares = []

#Numeros entre 1 y 1000
for i in range(100):
    numero = random.randint(1, 1000) 
    if numero % 2 == 0: lista_pares.append(numero) 
    else: lista_impares.append(numero) 

# Imprimir listas y tamaños
print("Lista de pares:", lista_pares)
print("Tamaño pares:", len(lista_pares))

print("Lista de impares:", lista_impares) 
print("Tamaño impares:", len(lista_impares))
