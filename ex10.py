from functools import reduce

def calcular_media_ponderada(dicionario):
    media_ponderada = lambda x: reduce(lambda acc, n: acc + n[0] * n[1], zip(x[:len(x)//2], x[len(x)//2:]), 0) / reduce(lambda acc, p: acc + p, x[len(x)//2:], 0) if sum(x[len(x)//2:]) != 0 else 0
    
    return {aluno: media_ponderada(notas) for aluno, notas in dicionario.items()}

entrada = eval(input("Digite um dicionário no formato {'Aluno1': [nota1, nota2, peso1, peso2], 'Aluno2': [nota1, nota2, peso1, peso2]}: "))


resultado = calcular_media_ponderada(entrada)
print("Médias ponderadas:", resultado)
