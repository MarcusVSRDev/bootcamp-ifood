def calcular_total(numeros):
    return sum(numeros)

def retornar_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero +1   
    return antecessor, sucessor

print(calcular_total([1, 2, 3, 4, 5]))
print(retornar_antecessor_e_sucessor(10))
# O retorno de uma função pode ser atribuído a variáveis
# e, se a função retornar mais de um valor, podemos atribuir a várias variáveis
# simultaneamente.
