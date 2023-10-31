clientes = []
while True:
    nome = input("Digite o nome completo do cliente: ")
    rg = input("Digite o RG do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    clientes.append([nome, rg, cpf, telefone])
    continuar = input("Deseja adicionar outro cliente? (s/n) ")
    if continuar.lower() != 's':
        break
for cliente in clientes:
    print(f"Nome: {cliente[0]}, RG: {cliente[1]}, CPF: {cliente[2]}, Telefone: {cliente[3]}")