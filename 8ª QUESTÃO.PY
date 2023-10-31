pares = []
impares = []
while True:
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    if len(pares) == 5:
        print(f"Lista de números pares: {pares}")
        pares = []
    if len(impares) == 5:
        print(f"Lista de números ímpares: {impares}")
        impares = []
    continuar = input("Deseja continuar? (s/n) ")
    if continuar.lower() != 's':
        break
if pares:
    print(f"Lista de números pares: {pares}")
if impares:
    print(f"Lista de números ímpares: {impares}")