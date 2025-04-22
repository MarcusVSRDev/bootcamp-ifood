#* Args = Tupla
#** Kwargs = Dicionário
#O nome do args e o kwargs são convencionais, mas podem ser alterados.

def exibir_poema(data_extenso, *args, **kwargs):
    text = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{text}\n\n{meta_dados}"
    print(mensagem)

exibir_poema("Zen of Python", 
             "Beautiful is better than ugly.", 
             autor = "Tim Peters", 
             ano = 2004,)
# Exemplo de uso de args e kwargs