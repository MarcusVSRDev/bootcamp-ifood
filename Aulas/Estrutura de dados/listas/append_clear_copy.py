lista = []

lista.append(1)
lista.append('python')
lista.append([40,30,20])
# Adiciona os elementos 1, 'python' e [40,30,20] na lista

print(lista) # [1, 'python', [40, 30, 20]]

lista = [1, 'python', [40, 30, 20]]

lista.clear()
# Limpa a lista, removendo todos os elementos

print(lista) # []   

lista = [1, 'python', [40, 30, 20]]

lista.copy()
# Faz uma cópia da lista, mas não altera a lista original

print(lista) # [1, 'python', [40, 30, 20]]

cores = ['azul', 'verde', 'amarelo']

cores.count ('azul') # 1
# Conta quantas vezes o elemento 'azul' aparece na lista cores

linguagens = ['python', 'java', 'c++']

print(linguagens) # ['python', 'java', 'c++']

linguagens.extend(['javascript', 'c#'])
# Adiciona os elementos 'javascript' e 'c#' na lista linguagens

print(linguagens) # ['python', 'java', 'c++', 'javascript', 'c#']

linguagens.index('java') # 1    
linguagens.index('c#') # 4  
# Retorna o índice do elemento 'java' e 'c#' na lista linguagens

linguagens = ['python', 'java', 'c++']

linguagens.pop() # Remove o último elemento da lista linguagens
linguagens.pop(1) # Remove o elemento na posição 1 da lista linguagens  

print(linguagens) # ['python']

linguagens = ['python', 'java', 'c++']

linguagens.remove('python') # Remove o elemento 'python' da lista linguagens

print(linguagens) # ['java', 'c++']

linguagens = ['python', 'java', 'c++']

linguagens.reverse() # Inverte a ordem dos elementos da lista linguagens

print(linguagens) # ['c++', 'java', 'python']

linguagens = ['python', 'java', 'c++']
linguagens.sort() # Ordena os elementos da lista linguagens em ordem alfabética

linguagens = ['python', 'java', 'c++']
linguagens.sort(reverse=True) # Ordena os elementos da lista linguagens em ordem alfabética inversa

linguagens = ['python', 'java', 'c++']
linguagens.sort(key=lambda x: len(x)) # Ordena os elementos da lista linguagens pelo tamanho das strings
# A lista linguagens será ordenada de acordo com o tamanho das strings, do menor para o maior

linguagens = ['python', 'java', 'c++']
linguagens.sort(key=lambda x: len(x), reverse=True) # Ordena os elementos da lista linguagens pelo tamanho das strings em ordem decrescente

linguagens = ['python', 'java', 'c++']
len(linguagens) # 3
# Retorna o número de elementos na lista linguagens

linguagens = ['python', 'java', 'c++']
sorted(linguagens, key=lambda x: len(x)) # Retorna uma nova lista ordenada pelo tamanho das strings, sem alterar a lista original

sorted(linguagens, key=lambda x: len(x), reverse=True) # Retorna uma nova lista ordenada pelo tamanho das strings em ordem decrescente, sem alterar a lista original
