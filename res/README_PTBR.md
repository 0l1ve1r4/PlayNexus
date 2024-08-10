![Atividade de commits](https://img.shields.io/github/commit-activity/m/iyksh/PlayNexus)
![Principal linguagem do GitHub](https://img.shields.io/github/languages/top/iyksh/PlayNexus?logo=python&label=)
[![Licença do GitHub](https://img.shields.io/github/license/iyksh/PlayNexus)](https://github.com/iyksh/PlayNexus/LICENSE)

# PlayNexus

> NOTA:
>
> Para o README em inglês, clique aqui: [![en](https://img.shields.io/badge/lang-en-green.svg)](../README.md)

## Introdução

PlayNexus é um clone de código aberto do Steam desenvolvido em Python 3.11.2+. O projeto tem como objetivo fornecer aos usuários uma plataforma completa de gerenciamento de jogos que permite:

- Gerenciar sua biblioteca de jogos (adicionar, remover, editar jogos)
- Lançar jogos de várias fontes (locais e não locais)

A interface gráfica é construída usando `customtkinter` para garantir uma experiência amigável ao usuário. O backend é alimentado por um banco de dados MySQL.

## Desenvolvedores do Projeto

| Categoria | Nome             |
| --------- | ---------------- |
| ALL       | Guilherme Santos |
| BACK-END  | Lucas, Franklin  |
| FRONT-END | Arthur, Mateus   |
| DATABASE  | [Seu Nome Aqui]  |

## Estrutura

```sh
├── README.md
├── res/                    # Imagens, sons, etc.
├── src/                    # Código fonte
│   ├── login/
│   ├── main.py
└── run.sh                  # Arquivo principal de execução
```


## Backlog do produto

> * Eu como administrador gostaria de cadastrar um jogo.
> * Eu como administrador gostaria de buscar um jogo cadastrado.
> * Eu como administrador gostaria de vizualizar informações sobre um jogo cadastrado, incluindo informações de quantidade de vendas e receita gerada.
> * Eu como usuário gostaria de criar uma conta.
> * Eu como usuário gostaria de buscar um jogo na loja.
> * Eu como usuário gostaria de vizualizar informações sobre um jogo na loja.
> * Eu como usuário gostaria de comprar um jogo na loja.
> * Eu como usuário gostaria de visualizar meu carrinho de compras na loja.
> * Eu como usuário gostaria de visualizar os jogos que estão na minha biblioteca.
> * Eu como usuário gostaria de iniciar um jogo da minha biblioteca.
> * Eu como usuário gostaria de ter um perfil visivel a outros usuáios.
> * Eu como usuário gostaria de buscar o perfil de outros usuários.
> * Eu como usuário gostaria de personalizar meu perfil.
> * Eu como usuário gostaria que outros usuários pudessem vizualizar em meu perfil os jogos que eu tenho em minha biblioteca e quais eu tenho jogado recentemente.

## Backlog da 1ª sprint

> * **Eu como administrador gostaria de cadastrar um jogo.**
>   * Estruturar o banco de dados para armazenar as informações dos jogos
>   * Criar o formulário de cadastro de jogos na interface gráfica
>   * Implementar validações no formulário de cadastro de jogos
>   * Desenvolver a lógica no backend para processar o cadastro dos jogos
>   * Realizar testes e ajustes para garantir que o processo de cadastro de jogos funcione corretamente
> * **Eu como usuário gostaria de criar uma conta.**
>   * Criar a estrutura do banco de dados para armazenamento de contas de usuários
>   * Desenvolver a interface de criação de contas de usuário
>   * Implementar as validações necessárias para garantir que os dados de entrada sejam corretos
>   * Desenvolver a lógica no backend para processar a criação de contas de usuários
>   * Testar o processo de criação de contas de usuários para assegurar seu funcionamento
> * **Eu como usuário gostaria de comprar um jogo na loja.**
>   * Estruturar o banco de dados para armazenar informações sobre as compras
>   * Desenvolver a interface de compra de jogos na loja
>   * Implementar a lógica no backend para processar as compras
>   * Testar todo o processo de compra para garantir que esteja funcionando corretamente
> * **Eu como usuário gostaria de visualizar os jogos que estão na minha biblioteca.**
>   * Configurar o banco de dados para armazenar as informações dos jogos na biblioteca do usuário
>   * Criar a interface de visualização da biblioteca de jogos do usuário
>   * Desenvolver a lógica no backend para gerenciar a visualização da biblioteca de jogos
>   * Realizar testes para garantir que a biblioteca de jogos seja exibida corretamente
> * **Eu como usuário gostaria de iniciar um jogo da minha biblioteca.**
>   * Estruturar o banco de dados para armazenar as informações de instalação dos jogos
>   * Desenvolver a interface para iniciar jogos a partir da biblioteca
>   * Implementar a lógica no backend para permitir a inicialização de jogos da biblioteca
>   * Testar e ajustar o processo de inicialização dos jogos para garantir que funcione corretamente
