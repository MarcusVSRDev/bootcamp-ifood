numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [par for par in numeros if par % 2 == 0]
# Outra forma de fazer a mesma coisa

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [num ** 2 for num in numeros]
# Outra forma de fazer a mesma coisa
