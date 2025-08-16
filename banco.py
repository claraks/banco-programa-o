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
  pr
