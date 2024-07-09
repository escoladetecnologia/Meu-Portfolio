# Menu principal
menu = (
    "[d] Depositar\n"
    "[s] Sacar\n"
    "[e] Extrato\n"
    "[u] Criar Usuário\n"
    "[c] Criar Conta Bancária\n"
    "[q] Sair\n\n"
    "=> "
)

# Variáveis globais para controle financeiro
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Dicionário para armazenar informações de usuários e suas contas
usuarios = {}

def depositar():
    global saldo, extrato
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar():
    global saldo, extrato, numero_saques
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso.")
    else:
        print("Operação falhou! O valor informado é inválido.")

def exibir_extrato():
    global extrato, saldo
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario():
    print("\n### Criação de Novo Usuário ###")
    cpf = input("Informe o CPF do usuário: ")
    nome = input("Informe o nome do usuário: ")  # Captura o nome do usuário
    endereco = input("Informe o endereço do usuário: ")
    telefone = input("Informe o telefone do usuário: ")

    # Verificar se o CPF já está registrado
    if cpf in usuarios:
        print("Usuário já cadastrado.")
        return
    
    usuarios[cpf] = {'nome': nome, 'endereco': endereco, 'telefone': telefone}
    print(f"Usuário criado com sucesso:\nCPF: {cpf}\nNome: {nome}\nEndereço: {endereco}\nTelefone: {telefone}")


def criar_conta_bancaria():
    print("\n### Abertura de Nova Conta Bancária ###")
    cpf = input("Informe o CPF do titular da conta: ")

    # Verificar se o CPF está registrado
    if cpf not in usuarios:
        print("Usuário não encontrado.")
        return
    
    nome_usuario = usuarios[cpf]['nome']  # Captura o nome do usuário

    # Agência fixa
    agencia = "0001"

    # Gerar número da conta automaticamente
    numero_conta = len(usuarios) * 1000 + 1  # Exemplo simples de geração automática

    # Salvar informações da conta
    usuarios[cpf]['conta_bancaria'] = {'agencia': agencia, 'numero_conta': numero_conta}

    print(f"Conta bancária criada com sucesso:\nAgência: {agencia}\nConta-Corrente: {numero_conta}\nTitular: {nome_usuario}\nCPF: {cpf}")



def main():
    while True:
        opcao = input(menu).strip().lower()

        if opcao == "d":
            depositar()
        elif opcao == "s":
            sacar()
        elif opcao == "e":
            exibir_extrato()
        elif opcao == "u":
            criar_usuario()
        elif opcao == "c":
            criar_conta_bancaria()
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
