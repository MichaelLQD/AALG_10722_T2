import random

def generar_palabra():
    palabra = ""
    for i in range(4):
        palabra += chr(random.randint(97, 122)) 
    return palabra

def crear_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(generar_palabra())
        matriz.append(fila)
    return matriz

def contarvoca(matriz):
    n = len(matriz)
    if n == 1:
        contador = 0
        for palabra in matriz[0]:
            for letra in palabra:
                if letra in "aeiou":
                    contador += 1
                    break
        return contador
    mitad = n // 2
    sub1 = [fila[:mitad] for fila in matriz[:mitad]]
    sub2 = [fila[mitad:] for fila in matriz[:mitad]]
    sub3 = [fila[:mitad] for fila in matriz[mitad:]]
    sub4 = [fila[mitad:] for fila in matriz[mitad:]]
    total = 0
    if sub1: total += contarvoca(sub1)
    if sub2: total += contarvoca(sub2)
    if sub3: total += contarvoca(sub3)
    if sub4: total += contarvoca(sub4)
    return total
n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
matriz = crear_matriz(n)
print("\nMatriz generada:\n")
for fila in matriz:
    print(' '.join(fila))
total = contarvoca(matriz)
print("\nCantidad de palabras con al menos una vocal:", total)

