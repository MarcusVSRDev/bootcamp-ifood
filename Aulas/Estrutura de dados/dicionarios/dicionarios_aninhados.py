contatos = {
    "marcus@email.com" : {"nome": "Marcus", "telefone": "1234-5678", "endereco": "Rua A, 123"},
    "giovana@email.com" : {"nome": "Giovana", "telefone": "9876-5432", "endereco": "Rua B, 456"},
    "chappie@email.com" : {"nome": "Chappie", "telefone": "5555-5555", "endereco": "Rua C, 789"},
    "vicente@email.co," : {"nome": "Vicente", "telefone": "4444-4444", "endereco": "Rua D, 101"},
}

contatos["marcus@email.com"]["telefone"] # Acessando o telefone do Marcus

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

# marcus@email.com : {'nome': 'Marcus', 'telefone': '1234-5678', 'endereco': 'Rua A, 123'}
# giovana@email.com : {'nome': 'Giovana', 'telefone': '9876-5432', 'endereco': 'Rua B, 456'}
# chappie@email.com : {'nome': 'Chappie', 'telefone': '5555-5555', 'endereco': 'Rua C, 789'}
