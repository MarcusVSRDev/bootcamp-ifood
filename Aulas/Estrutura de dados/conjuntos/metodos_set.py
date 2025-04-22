conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b)  # União dos conjuntos 
# {1, 2, 3, 4}

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b)  # Interseção dos conjuntos
# {2, 3}

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b)  # Diferença dos conjuntos
# {1}
conjunto_b.difference(conjunto_a)  # Diferença dos conjuntos
# {4}

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b)  # Diferença simétrica dos conjuntos
# {1, 4}
conjunto_b.symmetric_difference(conjunto_a)  # Diferença simétrica dos conjuntos
# {1, 4}

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b)  # Verifica se o conjunto_a é subconjunto do conjunto_b
# True
conjunto_b.issubset(conjunto_a)  # Verifica se o conjunto_b é subconjunto do conjunto_a
# False

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b)  # Verifica se o conjunto_a é superconjunto do conjunto_b
# False
conjunto_b.issuperset(conjunto_a)  # Verifica se o conjunto_b é superconjunto do conjunto_a
# True

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b)  # Verifica se os conjuntos não têm elementos em comum
# True
conjunto_a.isdisjoint(conjunto_c)  # Verifica se os conjuntos não têm elementos em comum
# False 

sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(1) # {1, 23, 25} (não adiciona o elemento repetido)

sorteio = {1, 23}
sorteio.clear() # Limpa o conjunto, tornando-o vazio

sorteio = {1, 23}
sorteio.copy() # Cria uma cópia do conjunto

sorteio = {1, 23}
sorteio.discard(23) # Remove o elemento 23 do conjunto, se ele existir
sorteio.discard(25) # Não gera erro se o elemento não existir no conjunto

sorteio = {1, 23}
sorteio.pop() # Remove e retorna um elemento aleatório do conjunto
sorteio.pop() # Se o conjunto estiver vazio, gera um erro

sorteio = {1, 23}
sorteio.remove(23) # Remove o elemento 23 do conjunto, se ele existir
sorteio.remove(25) # Gera um erro se o elemento não existir no conjunto

numeros = {1, 2, 3, 4, 5}
len(numeros) # Retorna o número de elementos do conjunto    

numeros = {1, 2, 3, 4, 5}
1 in numeros # Verifica se o elemento 1 está no conjunto  
# True
10 in numeros # Verifica se o elemento 10 está no conjunto
# False

