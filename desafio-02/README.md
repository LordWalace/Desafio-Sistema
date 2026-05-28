# Desafio 02 — Sistema Bancário Modularizado

Esta segunda etapa evolui o sistema bancário em Python com foco em organização, modularização e cadastro de usuários e contas.

## Objetivo

- Separar operações em funções reutilizáveis,
- Criar usuários identificados por CPF,
- Impedir duplicação de CPF,
- Criar contas correntes vinculadas a usuários existentes,
- Listar contas cadastradas.

## Funcionalidades

- `depositar` com validação de valor positivo
- `sacar` com limite diário e controle de saques
- `exibir_extrato` para mostrar histórico e saldo
- `criar_usuario` garantindo CPF único
- `criar_conta` vinculada a usuário cadastrado
- `listar_contas` exibindo dados da conta e titular

## Evolução em relação ao Desafio 01

O Desafio 02 representa a evolução da primeira versão usando funções Python para deixar o sistema mais organizado e fácil de manter.

- A primeira versão tratava apenas movimentações financeiras.
- Nesta versão, a lógica do banco é separada em funções independentes.
- O cadastro de usuários e a criação de contas tornam o sistema mais realista.

## Como usar

1. Abra o terminal na pasta `desafio-02`
2. Execute:

```bash
python desafio_sistema_bancario.py
```

## Estrutura

- `desafio_sistema_bancario.py`: código do segundo desafio, com funções para usuários, contas e operações bancárias.