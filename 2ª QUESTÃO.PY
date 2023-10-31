lista = []
for i in range(10):
    num = int(input("Digite um número: "))
    lista.append(num)
num_verificar = int(input("Digite um número para verificar: "))
if num_verificar in lista:
    print("O número está na lista.")
else:
    print("O número não está na lista.")