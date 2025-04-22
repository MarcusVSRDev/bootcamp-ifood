contatos = {
    "marcus@email.com" : {"nome": "Marcus", "telefone": "1234-5678", "endereco": "Rua A, 123"},
    "giovana@email.com" : {"nome": "Giovana", "telefone": "9876-5432", "endereco": "Rua B, 456"},
    "chappie@email.com" : {"nome": "Chappie", "telefone": "5555-5555", "endereco": "Rua C, 789"},
    "vicente@email.co," : {"nome": "Vicente", "telefone": "4444-4444", "endereco": "Rua D, 101"},
}

contatos.clear() # Limpa o dicionário, removendo todos os itens

contatos = {
    "marcus@email.com" : {"nome": "Marcus", "telefone": "1234-5678", "endereco": "Rua A, 123"},
    "giovana@email.com" : {"nome": "Giovana", "telefone": "9876-5432", "endereco": "Rua B, 456"},
    "chappie@email.com" : {"nome": "Chappie", "telefone": "5555-5555", "endereco": "Rua C, 789"},
    "vicente@email.co," : {"nome": "Vicente", "telefone": "4444-4444", "endereco": "Rua D, 101"},
}

copia = contatos.copy() # Cria uma cópia do dicionário

dict.fromkeys(["a", "b", "c"], 0) # Cria um dicionário com as chaves "a", "b" e "c" e o valor 0 para cada chave
# {'a': 0, 'b': 0, 'c': 0}

contatos = {
    "marcus@email.com" : {"nome": "Marcus", "telefone": "1234-5678", "endereco": "Rua A, 123"},
    "giovana@email.com" : {"nome": "Giovana", "telefone": "9876-5432", "endereco": "Rua B, 456"},
    "chappie@email.com" : {"nome": "Chappie", "telefone": "5555-5555", "endereco": "Rua C, 789"},
    "vicente@email.co," : {"nome": "Vicente", "telefone": "4444-4444", "endereco": "Rua D, 101"},
}

contatos["chave"] #KeyError: 'chave' não está no dicionário

contatos.get("chave") # Retorna None se a chave não existir no dicionário
contatos.get("chave", {}) # Retorna um dicionário vazio se a chave não existir no dicionário
contatos.get("marcus@email.com", {}) # Retorna o valor associado à chave "

contatos = {
    "marcus@email.com" : {"nome": "Marcus", "telefone": "1234-5678", "endereco": "Rua A, 123"},
    "giovana@email.com" : {"nome": "Giovana", "telefone": "9876-5432", "endereco": "Rua B, 456"},
    "chappie@email.com" : {"nome": "Chappie", "telefone": "5555-5555", "endereco": "Rua C, 789"},
    "vicente@email.co," : {"nome": "Vicente", "telefone": "4444-4444", "endereco": "Rua D, 101"},
}

contatos.items() # Retorna uma lista de tuplas com as chaves e valores do dicionário
contatos.keys() # Retorna uma lista com as chaves do dicionário
contatos.values() # Retorna uma lista com os valores do dicionário

contatos = {
    "marcus@email.com" : {"nome": "Marcus", "telefone": "1234-5678", "endereco": "Rua A, 123"},
    "giovana@email.com" : {"nome": "Giovana", "telefone": "9876-5432", "endereco": "Rua B, 456"},
    "chappie@email.com" : {"nome": "Chappie", "telefone": "5555-5555", "endereco": "Rua C, 789"},
    "vicente@email.co," : {"nome": "Vicente", "telefone": "4444-4444", "endereco": "Rua D, 101"},
}

contatos.pop("marcus@email.com") 
contatos.pop("marcus@email.com", {}) # Retorna um dicionário vazio se a chave não existir no dicionário
contatos.popitem() # Remove e retorna o último item adicionado ao dicionário

contatos = {
    "marcus@email.com" : {"nome": "Marcus", "telefone": "1234-5678", "endereco": "Rua A, 123"},
    "giovana@email.com" : {"nome": "Giovana", "telefone": "9876-5432", "endereco": "Rua B, 456"},
    "chappie@email.com" : {"nome": "Chappie", "telefone": "5555-5555", "endereco": "Rua C, 789"},
    "vicente@email.co," : {"nome": "Vicente", "telefone": "4444-4444", "endereco": "Rua D, 101"},
}

contatos.setdefault("nome", "Marcus") # Adiciona a chave "nome" com o valor "Marcus" se a chave não existir no dicionário
contatos.setdefault("idade", 25) # Adiciona a chave "idade" com o valor 25 se a chave não existir no dicionário

contatos = {
    "marcus@email.com" : {"nome": "Marcus", "telefone": "1234-5678", "endereco": "Rua A, 123"},
    "giovana@email.com" : {"nome": "Giovana", "telefone": "9876-5432", "endereco": "Rua B, 456"},
    "chappie@email.com" : {"nome": "Chappie", "telefone": "5555-5555", "endereco": "Rua C, 789"},
    "vicente@email.co," : {"nome": "Vicente", "telefone": "4444-4444", "endereco": "Rua D, 101"},
}

contatos.update({"marcus@email.com" : {"nome": "Marcus", "telefone": "1234-5678", "endereco": "Rua A, 123"}}) # Atualiza o dicionário com os valores do dicionário passado como parâmetro
contatos.update({"joão@email.com" : {"nome": "João", "telefone": "1111-1111", "endereco": "Rua E, 111"}}) # Adiciona o dicionário passado como parâmetro ao dicionário original

contatos = {
    "marcus@email.com" : {"nome": "Marcus", "telefone": "1234-5678", "endereco": "Rua A, 123"},
    "giovana@email.com" : {"nome": "Giovana", "telefone": "9876-5432", "endereco": "Rua B, 456"},
    "chappie@email.com" : {"nome": "Chappie", "telefone": "5555-5555", "endereco": "Rua C, 789"},
    "vicente@email.co," : {"nome": "Vicente", "telefone": "4444-4444", "endereco": "Rua D, 101"},
}

"marcus@email.com" in contatos # Retorna True se a chave existir no dicionário
"felipe@email.com" in contatos # Retorna False se a chave não existir no dicionário

contatos = {
    "marcus@email.com" : {"nome": "Marcus", "telefone": "1234-5678", "endereco": "Rua A, 123"},
    "giovana@email.com" : {"nome": "Giovana", "telefone": "9876-5432", "endereco": "Rua B, 456"},
    "chappie@email.com" : {"nome": "Chappie", "telefone": "5555-5555", "endereco": "Rua C, 789"},
    "vicente@email.co," : {"nome": "Vicente", "telefone": "4444-4444", "endereco": "Rua D, 101"},
}

del contatos["marcus@email.com"] ["telefone"] # Remove a chave "telefone" do dicionário associado à chave
del contatos["chappie@email.com"] # Remove o dicionário associado à chave 
del contatos["chave"] # KeyError: 'chave' não está no dicionário
