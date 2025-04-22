#Atualização do desafio de criar um sistema bancário com Python
# O código abaixo é um sistema bancário simples que permite ao usuário depositar, sacar e visualizar o extrato da conta.
# Criar a função "Criar Usuário" e "Criar Conta" para o sistema bancário, permitindo que os usuários criem contas e façam transações.
# O código foi atualizado para incluir melhorias na validação de entradas e na estrutura geral do código.   


# Função para criar um usuário no sistema bancário
def criar_usuario(usuarios):
    cpf = input("Digite o CPF do usuário: ")
    if cpf in usuarios:
        print("Usuário já cadastrado!")
        return usuarios
    else:
        nome = input("Digite o nome do usuário: ")
        endereco = input("Digite o endereço do usuário: ")
        telefone = input("Digite o telefone do usuário: ")
        
    usuario = {
        "cpf": cpf,
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone
    }
    usuarios[cpf] = usuario
    print(f"Usuário {nome} criado com sucesso!")
    return usuarios
        

# Função para criar uma conta bancária
def criar_conta(usuarios, contas):
    cpf = input("Digite o CPF do usuário para criar a conta: ")
    
    if cpf not in usuarios:
        print("Usuário não encontrado!")
        return contas
    
    numero_conta = len(contas) + 1001 # Inicia a numeração das contas em 1001
    while numero_conta in contas:
        numero_conta += 1 # Garante que o número da conta seja único
    saldo = 0.0
    
    conta = {
        "numero": numero_conta,
        "cpf": cpf,
        "saldo": saldo
    }
    
    contas[numero_conta] = conta
    print(f"Conta número {numero_conta} criada com sucesso!")
    return contas

def saque(*, contas, usuarios):
    limite_saques = 3
    saques_realizados = 0
    numero_conta = int(input("Digite o número da conta: "))
    valor = float(input("Digite o valor do saque: "))

    if numero_conta in contas:
        if contas[numero_conta]["saldo"] >= valor:
            contas[numero_conta]["saldo"] -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            saques_realizados += 1
            if saques_realizados > limite_saques:
                print("Limite de saques diários atingido.")
        else:
            print("Saldo insuficiente para realizar o saque.")
    else:
        print("Conta não encontrada.")

def deposito(*, contas):
    numero_conta = int(input("Digite o número da conta: "))
    valor = float(input("Digite o valor do depósito: "))

    if numero_conta in contas:
        contas[numero_conta]["saldo"] += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Conta não encontrada.")

def extrato(contas, usuarios):
    numero_conta = int(input("Digite o número da conta: "))

    if numero_conta in contas:
        saldo = contas[numero_conta]["saldo"]
        print(f"Extrato da conta {numero_conta}: R$ {saldo:.2f}")
    else:
        print("Conta não encontrada.")

def listar_contas(contas):
    print("Contas cadastradas:")
    for numero_conta, conta in contas.items():
        print(f"Conta número {numero_conta}: CPF {conta['cpf']}, Saldo R$ {conta['saldo']:.2f}")

def main():
    usuarios = {}
    contas = {}

    while True:
        print("\nSistema Bancário")
        print("1. Criar Usuário")
        print("2. Criar Conta")
        print("3. Saque")
        print("4. Depósito")
        print("5. Extrato")
        print("6. Listar Contas")
        print("7. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            usuarios = criar_usuario(usuarios)
        elif opcao == 2:
            contas = criar_conta(usuarios, contas)
        elif opcao == 3:
            saque(contas=contas, usuarios=usuarios)
        elif opcao == 4:
            deposito(contas=contas)
        elif opcao == 5:
            extrato(contas=contas, usuarios=usuarios)
        elif opcao == 6:
            listar_contas(contas=contas)
        elif opcao == 7:
            break
        else:
            print("Opção inválida! Tente novamente.")

main()

# Fim do código