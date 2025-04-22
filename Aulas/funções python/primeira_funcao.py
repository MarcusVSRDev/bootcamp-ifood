def exibir_mensagem():
    print("Olá, mundo!")

def exibir_mensagem_com_parametro(nome):
    print(f"Seja bem-vindo(a), {nome}!")

def exibir_mensagem_com_parametro2(nome ="Anônimo"):
    print(f"Seja bem-vindo(a), {nome}!")

exibir_mensagem()
exibir_mensagem_com_parametro("Marcus")
exibir_mensagem_com_parametro2()