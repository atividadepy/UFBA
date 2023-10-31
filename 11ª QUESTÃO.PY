codigo = int(input("Digite um código (0 para terminar, 1 para ordem direta, 2 para ordem inversa): "))
while codigo != 0:
    lista = [float(input("Digite um número real: ")) for _ in range(15)]
    if codigo == 1:
        print(lista)
    elif codigo == 2:
        print(lista[::-1])
    codigo = int(input("Digite um código (0 para terminar, 1 para ordem direta, 2 para ordem inversa): "))