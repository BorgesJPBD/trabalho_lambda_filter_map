elementos_dobrados = []

user = input("Digite uma sequência de números separados por espaço: ")
numeros = list(map(int, user.split()))
elementos_dobrados = list(map(lambda x: x * 2, numeros))
print("O dobro da sequência é: ", elementos_dobrados)