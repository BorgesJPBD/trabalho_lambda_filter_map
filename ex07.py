def agrupar_numeros(lista):
    return "Positivos" , list(filter(lambda x: x > 0 , lista)) , "negativos" , list(filter(lambda x: x < 0 , lista)) , "zeros" , list(filter(lambda x: x == 0 , lista))
entrada = input("Digite uma sequencia de numeros separados por espaço: ")

lista = list(map(int, entrada.split()))
print(agrupar_numeros(lista))