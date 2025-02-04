pares = []
user = input("Digite uma sequência de números separados por espaço: ")
numeros_pares = numeros = list(map(int, user.split()))
numeros_filtrados = list(filter(lambda x: x%2 == 0, numeros_pares))

print("Os números pares são: ", numeros_filtrados)