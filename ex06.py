def separar_pares_impares(lista):
    pares = list(filter(lambda x: x % 2 == 0, lista))
    impares = list(filter(lambda x: x % 2 == 1, lista))
    
    return {"pares": pares, "ímpares": impares}

entrada_usuario = input("Digite uma lista de números inteiros separados por espaço: ")

lista_numeros = list(map(int, entrada_usuario.split()))

resultado = separar_pares_impares(lista_numeros)
print("Resultado:", resultado)