def nomes(lista):
    
    lista = list(filter(lambda x: len(x) > 5, lista))
    return lista

entrada = input("Digite uma sequencia de numeros separados por espaço e acrescentando virgula entre eles: ")
lista = list(map(str.strip, entrada.split(',')))
print (nomes(lista))
    