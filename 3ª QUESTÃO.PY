lista = []
positivos = 0
negativos = 0
for i in range(10):
    num = float(input("Digite um número: "))
    lista.append(num)
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
media = sum(lista) / len(lista)
print("Média dos elementos: ", media)
print("Maior elemento: ", max(lista))
print("Menor elemento: ", min(lista))
print("Quantidade de elementos positivos: ", positivos)
print("Quantidade de elementos negativos: ", negativos)