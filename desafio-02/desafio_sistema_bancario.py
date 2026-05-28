"""Desafio 02 - Sistema bancário modularizado em Python.

Esta versão evolui o sistema bancário para incluir cadastro de usuários,
criação de contas vinculadas e separação de responsabilidades em funções.
"""

def depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("Operação falhou! O valor do depósito deve ser positivo.")
        return saldo, extrato

    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor <= 0:
        print("Operação falhou! O valor do saque deve ser positivo.")
        return saldo, extrato, numero_saques

    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
        return saldo, extrato, numero_saques

    if valor > limite:
        print(f"Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}.")
        return saldo, extrato, numero_saques

    if numero_saques >= limite_saques:
        print("Operação falhou! Limite de saques diários atingido.")
        return saldo, extrato, numero_saques

    saldo -= valor
    extrato += f"Saque:\t\tR$ {valor:.2f}\n"
    numero_saques += 1
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========\n")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato, end="")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==============================\n")


def criar_usuario(usuarios):
    nome = input("Informe o nome do usuário: ").strip()
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    cpf = input("Informe o CPF (somente números): ").strip()
    endereco = input("Informe o endereço (rua, número, bairro, cidade/UF): ").strip()

    cpf_numeros = "".join([caractere for caractere in cpf if caractere.isdigit()])

    usuario_existente = any(usuario["cpf"] == cpf_numeros for usuario in usuarios)
    if usuario_existente:
        print("Já existe usuário com este CPF.")
        return

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf_numeros,
        "endereco": endereco,
    }

    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do cliente para criar conta: ").strip()
    cpf_numeros = "".join([caractere for caractere in cpf if caractere.isdigit()])

    usuario = None
    for item in usuarios:
        if item["cpf"] == cpf_numeros:
            usuario = item
            break

    if usuario is None:
        print("Usuário não encontrado. Crie um usuário antes de abrir uma conta.")
        return None

    conta = {
        "agencia": agencia,
        "numero_conta": f"{numero_conta:04d}",
        "usuario": usuario,
    }

    print("Conta criada com sucesso!")
    return conta


def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        usuario = conta["usuario"]
        print("\n------------------------------")
        print(f"Agência:\t{conta['agencia']}")
        print(f"Conta:\t\t{conta['numero_conta']}")
        print(f"Titular:\t{usuario['nome']}")
        print(f"CPF:\t\t{usuario['cpf']}")
        print(f"Nascimento:\t{usuario['data_nascimento']}")
        print(f"Endereço:\t{usuario['endereco']}")
    print("------------------------------")


def menu():
    return (
        "\n=== BANCO DIO - DESAFIO 02 ===\n"
        "1 - Depositar\n"
        "2 - Sacar\n"
        "3 - Extrato\n"
        "4 - Criar usuário\n"
        "5 - Criar conta\n"
        "6 - Listar contas\n"
        "7 - Sair\n"
    )


def main():
    saldo = 0.0
    limite = 500.0
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    usuarios = []
    contas = []
    agencia = "0001"
    numero_conta = 1

    while True:
        opcao = input(menu()).strip()

        if opcao == "1":
            try:
                valor = float(input("Informe o valor do depósito: ").strip())
            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            try:
                valor = float(input("Informe o valor do saque: ").strip())
            except ValueError:
                print("Valor inválido. Tente novamente.")
                continue

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=limite_saques,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            conta = criar_conta(agencia, numero_conta, usuarios)
            if conta is not None:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            print("Encerrando o sistema. Obrigado por utilizar o Banco DIO.")
            break

        else:
            print("Opção inválida. Selecione uma opção válida.")


if __name__ == "__main__":
    main()
