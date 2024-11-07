import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova Conta
    [5]\tNovo Usuario
    [0]\tSair
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado!")
    else:
        print("Operação inválida! Por favor verifique o valor informado!")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo               
    excedeu_limite = valor > limite               
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente!")
    elif excedeu_limite:
        print("Operação falhou! Você excedeu o limite!")
    elif excedeu_saques:
        print("Operação falhou! Você excedeu o limite de saques!")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido!")

    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios): 
    nome = input("Informe seu Nome Completo: ")
    data_nascimento = input("Informe sua Data de Nascimento: ")
    endereco = input("Digite seu endereço: ")
    cpf = input("Digite seu CPF: ")
    usuario = filtrar_contas(cpf, usuarios)

    if usuario:
        print("CPF já cadastrado!")
        return

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário criado com sucesso!")

def filtrar_contas(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_contas(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado!")

def main():
    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input('Informe o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':  
            valor = float(input('Informe o valor do saque: '))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == '3':
            mostrar_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == '5':
            criar_usuario(usuarios)

        elif opcao == '0':
            break

        else:
            print("Operação inválida, por favor selecione novamente a opção desejada")

main()
