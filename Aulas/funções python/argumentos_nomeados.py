def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro salvo: {marca} {modelo} {ano} {placa}")

salvar_carro("Fusca", "Fusca", 1970, "ABC-1234")
salvar_carro(ano=1970, modelo="Fusca", marca="Fusca", placa="ABC-1234")
salvar_carro(**{"marca": "Fusca", "modelo": "Fusca", "ano": 1970, "placa": "ABC-1234"})
# Exemplo de uso de argumentos nomeados em Python