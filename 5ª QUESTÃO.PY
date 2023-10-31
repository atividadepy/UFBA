import math

def ler_vetor(n):
    vetor = []
    for i in range(n):
        num = float(input(f"Digite o elemento {i+1}: "))
        vetor.append(num)
    return vetor

def calcular_norma(vetor):
    return math.sqrt(sum([i**2 for i in vetor]))

def calcular_soma(vetores):
    return [sum(x) for x in zip(*vetores)]

n = int(input("Digite o tamanho dos vetores: "))
vetores = [ler_vetor(n) for _ in range(3)]
normas = [calcular_norma(v) for v in vetores]
print(f"Vetor com maior norma: Vetor {normas.index(max(normas)) + 1}")
print(f"Vetor soma: {calcular_soma(vetores)}")