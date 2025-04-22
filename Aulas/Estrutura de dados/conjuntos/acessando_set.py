numeros = {1, 2, 3, 4, 5}
# Não é possível acessar os elementos de um set diretamente, pois não possuem índice
# Para acessar os elementos de um set, é necessário convertê-lo para uma lista

numeros = list(numeros)
print(numeros[0])  # Acessando o primeiro elemento  

carros = {'Fusca', 'Civic', 'Palio'}

for carro in carros:
    print(carro)  # Acessando os elementos do set com um loop for