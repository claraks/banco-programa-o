contas = []

def criar_conta():
    print("\n--- Criar Conta ---")
    nome = input("Nome Completo: ")
    numero = input("Número da Conta: ")
    senha = input("Senha: ")
    saldo = float(input("Depósito inicial: R$ "))

    conta = {"nome": nome, "numero": numero, "senha": senha, "saldo": saldo}
    contas.append(conta)
    print(f"Conta criada com sucesso para {nome}!\n")

def login():
    print("\n--- Login ---")
    numero = input("Número da conta: ")
    senha = input("Senha: ")

    for conta in contas:
        if conta["numero"] == numero and conta["senha"] == senha:
            print(f"\nBem-vindo(a), {conta['nome']}!\n")
            return conta
    print("Conta ou senha inválida.\n")
    return None

def sacar(conta):
    print("\n--- Saque ---")
    valor = float(input("Valor do saque: R$ "))
    taxa = 2.5
    if conta["saldo"] >= valor + taxa:
        conta["saldo"] -= valor + taxa
        print(f"Saque de R${valor:.2f} realizado. (Taxa R${taxa:.2f})\n")
    else:
        print("Saldo insuficiente.\n")

def depositar(conta):
    print("\n--- Depósito ---")
    valor = float(input("Valor do depósito: R$ "))
    conta["saldo"] += valor
    print(f"Depósito de R${valor:.2f} realizado!\n")

def transferir(conta_origem):
    print("\n--- Transferência ---")
    destino = input("Número da conta de destino: ")
    valor = float(input("Valor da transferência: R$ "))
    taxa = 1.0

    for conta in contas:
        if conta["numero"] == destino:
            if conta_origem["saldo"] >= valor + taxa:
                conta_origem["saldo"] -= valor + taxa
                conta["saldo"] += valor
                print(f"Transferência de R${valor:.2f} feita para {conta['nome']}! (Taxa R${taxa:.2f})\n")
            else:
                print("Saldo insuficiente.\n")
            return
    print("Conta de destino não encontrada.\n")

def ver_saldo(conta):
    print(f"\nSaldo atual: R${conta['saldo']:.2f}\n")

def menu_conta(conta):
    while True:
        print("\n--- Menu da Conta ---")
        print("1. Sacar")
        print("2. Depositar")
        print("3. Transferir")
        print("4. Ver saldo")
        print("5. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            sacar(conta)
        elif opcao == "2":
            depositar(conta)
        elif opcao == "3":
            transferir(conta)
        elif opcao == "4":
            ver_saldo(conta)
        elif opcao == "5":
            print("Saindo da conta...\n")
            break
        else:
            print("Opção inválida.\n")

def menu():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Criar Conta")
        print("2. Login")
        print("3. Sair")
        escolha = input("Escolha: ")

        if escolha == "1":
            criar_conta()
        elif escolha == "2":
            conta = login()
            if conta:
                menu_conta(conta)
        elif escolha == "3":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida.\n")

menu()

