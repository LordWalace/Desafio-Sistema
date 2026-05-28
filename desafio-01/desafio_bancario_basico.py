"""Desafio 01 - Sistema bancário básico em Python.

Este módulo implementa operações financeiras simples: depósito, saque e extrato.
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


def menu():
    return (
        "\n=== BANCO DIO - DESAFIO 01 ===\n"
        "1 - Depositar\n"
        "2 - Sacar\n"
        "3 - Extrato\n"
        "4 - Sair\n"
    )


def main():
    saldo = 0.0
    limite = 500.0
    extrato = ""
    numero_saques = 0
    limite_saques = 3

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
            print("Encerrando o sistema. Obrigado por utilizar o Banco DIO.")
            break

        else:
            print("Opção inválida. Selecione uma opção válida.")


if __name__ == "__main__":
    main()
