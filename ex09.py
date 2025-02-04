def calcular_media(tupla):
    return sum(tupla) / len(tupla)

def filtrar_tuplas(lista):
    return list(filter(lambda tupla: calcular_media(tupla) > 5, lista))


entrada = input("Digite uma lista de tuplas (ex: (1,2,3) (4,5,6)): ")

try:
    tuplas = [tuple(map(int, t.strip("()").split(","))) for t in entrada.split()]
    resultado = filtrar_tuplas(tuplas)
    print("Tuplas cuja média dos valores é maior que 5:", resultado)
except ValueError:
    print("Erro: Certifique-se de inserir tuplas no formato correto, ex: (1,2,3) (4,5,6)")
