pacientes = []
idades = []
indenizacoes = []
while True:
    nome = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    indenizacao_base = float(input("Digite o valor base da indenização: "))
    if idade <= 12:
        reajuste = 0.3
    elif 13 <= idade <= 49:
        reajuste = 0.1
    elif 50 <= idade <= 65:
        reajuste = 0.15
    else:
        reajuste = 0.35
    indenizacao_reajustada = indenizacao_base * (1 + reajuste)
    pacientes.append(nome)
    idades.append(idade)
    indenizacoes.append(indenizacao_reajustada)
    continuar = input("Deseja adicionar outro paciente? (s/n) ")
    if continuar.lower() != 's':
        break
for i in range(len(pacientes)):
    print(f"Paciente: {pacientes[i]}, Idade: {idades[i]}, Indenização: {indenizacoes[i]}")