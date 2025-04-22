def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano = 1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #Válido

criar_carro(1999, "Palio", "ABC-1234", "Fiat", "1.0", "Gasolina") #Inválido, pois os parâmetros não estão nomeados  
