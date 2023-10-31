lista = [int(input("Digite um número: ")) for _ in range(10)]
pares = len([num for num in lista if num % 2 == 0])
print(f"Quantidade de números pares: {pares}")