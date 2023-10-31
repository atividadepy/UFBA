a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
lista = [int(input("Digite um número: ")) for _ in range(int(input("Digite o tamanho da lista: ")))]
contagem = len([num for num in lista if a <= num <= b])
print(f"Quantidade de elementos no intervalo [{a}; {b}]: {contagem}")