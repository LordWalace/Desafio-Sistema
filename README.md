# Desafio Sistema Bancário

Solução em Python para o desafio "Otimizando o Sistema Bancário com Funções Python" da DIO.

## Arquivo

- `desafio_sistema_bancario.py`: implementa o sistema bancário sem orientação a objetos, com funções puras controladas por `main()`.

## Uso

Execute o script com Python 3:

```bash
python desafio_sistema_bancario.py
```

## Funcionalidades

- Depósito com validação de valor positivo
- Saque com limite diário de 3 operações e valor máximo de R$ 500
- Exibição de extrato
- Criação de usuário com CPF único (apenas números)
- Criação de conta vinculada a usuário existente
- Listagem de contas cadastradas

## Regras atendidas

- Sem classes, apenas funções
- `depositar(saldo, valor, extrato, /)` recebe argumentos apenas por posição
- `sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)` recebe argumentos apenas por nome
- `exibir_extrato(saldo, /, *, extrato)` recebe saldo por posição e extrato por nome
- CPF armazenado apenas com números
- Conta criada apenas para usuário existente
