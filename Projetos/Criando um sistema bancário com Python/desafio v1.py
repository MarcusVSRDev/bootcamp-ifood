menu = """
Escolha uma das opções abaixo:

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

==>"""

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    # Definindo o que cada opção faz
    if opcao not in ["1", "2", "3", "4"]:
        # Verificando se o usuário digitou uma opção válida
        print("Opção inválida! Tente novamente.")
        # Se não, pede para tentar novamente
        continue
        # Se sim, continua o código
        
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
        # Verifica se o valor do depósito é maior que 0
        # Se sim, adiciona o valor ao saldo e atualiza o extrato
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
        # Se não, informa que o valor é inválido

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        if numero_de_saques < LIMITE_SAQUES and valor <= saldo and valor <= limite:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            if numero_de_saques >= LIMITE_SAQUES:
                print("Número máximo de saques atingido.")
            # Se o número de saques for maior que o limite, informa que o número máximo foi atingido
            elif valor > saldo:
                print("Saldo insuficiente.")
            # Se o valor do saque for maior que o saldo, informa que o saldo é insuficiente
            elif valor > limite:
                print("Valor acima do limite de saque.")
            # Se o valor do saque for maior que o limite, informa que o valor é acima do limite de saque

    elif opcao == "3":
        print("=== Extrato ===")
        if extrato == "":
            print("Nenhum movimento realizado.")
        # Se o extrato estiver vazio, informa que nenhum movimento foi realizado   
        else:
            print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        # Se não, imprime o extrato e o saldo atual

    elif opcao == "4":
        print("Saindo...")
        break
        # Se a opção for 4, informa que está saindo e encerra o loop
        # e o programa

# Fim do código