salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_bonus(1000) # 3000
print(salario) # 3000
# A função salario_bonus altera a variável global salario, adicionando o bônus a ela.    
