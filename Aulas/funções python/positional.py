def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Fusca', 1970, 'ABC-1234', 'Volkswagen', '1.3', 'Gasolina') #Válido
# O caractere '/' indica que os parâmetros à esquerda são posicionais
# e não podem ser passados como nomeados. Isso significa que você deve passar
# esses parâmetros na ordem correta, sem usar os nomes dos parâmetros.

criar_carro(modelo = "Palio", ano = 2000, placa = "XYZ-5678", marca = "Fiat", motor = "1.0", combustivel = "Etanol") #Inválido