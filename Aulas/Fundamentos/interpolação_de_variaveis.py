#Metodo %s de formatação de strings
nome = "Marcus"
idade = 23
profissao = "Cientista de dados"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

#Metodo format() de formatação de strings
nome = "Marcus"
idade = 23
profissao = "Cientista de dados"
linguagem = "Python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado no curso de {3}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

#Metodo f-strings de formatação de strings (Python 3.6+)
nome = "Marcus"
idade = 23
profissao = "Cientista de dados"
linguagem = "Python"

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")

PI = 3.14159265358979323846

print(f"PI é aproximadamente {PI:.2f}.")

print(f"Valor de PI: {PI:10.2f}")