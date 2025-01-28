def dobrar_elementos(numbers):
    return [x * 2 for x in numbers]    

user =  input("Digite uma sequência de números separados por espaço: ")

calcular_função = list(map(int, user.split()))

resultado = dobrar_elementos(calcular_função)
print ("O dobro da sequência é: ", resultado)
