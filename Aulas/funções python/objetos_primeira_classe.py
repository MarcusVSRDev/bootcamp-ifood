def somar(a, b):
    return a + b

def exibir_resultado (a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação é: {resultado}')    

exibir_resultado(10, 5, somar) # Resultado da operação é: 15    
# A função somar é passada como argumento para a função exibir_resultado, que a executa com os parâmetros 10 e 5.   