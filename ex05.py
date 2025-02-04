def elevar_quadrado(lista):
    return list(map(lambda x: x**2, lista))

entrada = input("Digite uma sequencia de numeros para elevar ao quadrado separados por espaço: ")

lista = list(map(int, entrada.split()))
sequencia = sorted (elevar_quadrado(lista))

print (sequencia)
