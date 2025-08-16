contas = []

def criar_conta():
  print("\n--- Criar Conta ---")
  nome = input("Nome Completo: ")
  numero = input("Número da Conta: ")
  senha = input("Senha: ")
  saldo = float(input("Depósito inicial: R$ ")

  conta = {"nome": nome, "numero": numero, "senha": senha, "saldo": saldo}
  contas.append(conta)
  print(f"Conta criada com sucesso {nome}!\n")
  
def login():
  print("\n--- Login ---")
  numero = input ("Número da conta: ")
  senha = input("Senha: ")

  for conta in contas:
    if conta["numero] == numero and conta["senha"]== senha:
        print(f"\n  Bem-vindo(a), {conta['nome']}!\n)
        return conta
  print("Conta ou senha inválida. \n")
  return None

def sacar(conta): 
  print("\n--- Sacar ---")
  valor = float(input("Valor do saque: R$ "))
  taxa = 2.5
  if conta["saldo"] >= valor + taxa: 
      conta["saldo"] -= valor + taxa
      print (f"Saque de R${valor:.2f} realiado. ("Taxa de R${taxa:.2f)\n")
  else:
    print("Saldo insufiente.\n")

def depositar(conta):
  print("\n--- Depósito ---")
  valor = float(input("Valor do depósito: R$ "))
  conta["saldo"] += valor
  print(f"Depósito de R${valor:.2f} realizado!\n")

def transferir(conta_origem):
  print("\n--- Transferência ---")
  destino = input("Conta de destino: ")
  valor = float(input("Valor de transferência: R$ "))
  taxa = 1.0
  
