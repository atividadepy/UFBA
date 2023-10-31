gabarito = [input("Digite a resposta da questão {}: ".format(i+1)) for i in range(20)]
for _ in range(50):
    nome = input("Digite o nome do aluno: ")
    respostas = [input("Digite a resposta da questão {}: ".format(i+1)) for i in range(20)]
    acertos = sum([g == r for g, r in zip(gabarito, respostas)])
    nota_final = acertos * 0.5
    if nota_final >= 6:
        print(f"{nome} - APROVADO - Nota final: {nota_final}")
    else:
        print(f"{nome} - REPROVADO - Nota final: {nota_final}")