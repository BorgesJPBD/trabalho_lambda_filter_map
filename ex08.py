from functools import reduce
def soma_letras(lista):
    return reduce (lambda x, y: x + len(y), lista , 0)
entrada = input("Digite uma sequencia de letras separadas por espaço: ")
lista = list(map(str, entrada.split()))
print (soma_letras(lista))
    