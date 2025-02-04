from functools import reduce

def soma_elementos(lista):
    return reduce(lambda x , y: x + y, lista)
entrada = input("Digite uma sequencia de numeros separados por espaço: ")
lista = list(map(int, entrada.split()))

print(soma_elementos(lista))


