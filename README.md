![Commit activity](https://img.shields.io/github/commit-activity/m/iyksh/PlayNexus)
![GitHub top language](https://img.shields.io/github/languages/top/iyksh/PlayNexus?logo=python&label=)
[![GitHub license](https://img.shields.io/github/license/iyksh/PlayNexus)](https://github.com/iyksh/PlayNexus/LICENSE)
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](./res/README_PTBR.md)

# PlayNexus

> NOTA:
>
> Para este arquivo em Português, clique aqui no ícone acima.

## Introduction

PlayNexus is an open-source Steam clone developed in Python 3.11.2+. The project aims to provide users with a comprehensive game management platform that allows them to:

- Browse and purchase computer games in a user-friendly store;
- Manage their game library (list, add, remove and edit);
- Create a custom profile and interact with other players;
- And play a countless games and have fun like never before.

The graphical interface is built using `customtkinter` to ensure a user-friendly experience. The backend is powered by a MySQL database.

## Project Devs

| Category  | Name             |
| --------- | ---------------- |
| ALL       | Guilherme Santos |
| BACK-END  | Lucas, Franklin  |
| FRONT-END | Arthur, Mateus   |

## Structure

```sh
├── README.md
├── res/                    # Images, sounds, etc.
├── src/                    # Source code
│   ├── login/
│   ├── main.py
└── run.sh                  # Main running file
```

## Product Backlog

> * As an administrator, I would like to register a game.
> * As an administrator, I would like to search for a registered game.
> * As an administrator, I would like to view information about a registered game, including sales quantity and revenue generated.
> * As a user, I would like to create an account.
> * As a user, I would like to search for a game in the store.
> * As a user, I would like to view information about a game in the store.
> * As a user, I would like to purchase a game in the store.
> * As a user, I would like to view my shopping cart in the store.
> * As a user, I would like to view the games that are in my library.
> * As a user, I would like to start a game from my library.
> * As a user, I would like to have a profile visible to other users.
> * As a user, I would like to search for other users' profiles.
> * As a user, I would like to customize my profile.
> * As a user, I would like other users to be able to view on my profile the games I have in my library and which ones I have recently played.

## Sprint 1 Backlog

> * **As an administrator, I would like to register a game.**
>   * Structure the database to store game information
>   * Create the game registration form in the graphical interface
>   * Implement validations in the game registration form
>   * Develop the backend logic to process game registration
>   * Conduct tests and adjustments to ensure the game registration process works correctly
> * **As a user, I would like to create an account.**
>   * Structure the database for storing user accounts
>   * Develop the user account creation interface
>   * Implement necessary validations to ensure input data is correct
>   * Develop the backend logic to process user account creation
>   * Test the account creation process to ensure it works properly
> * **As a user, I would like to purchase a game in the store.**
>   * Structure the database to store purchase information
>   * Develop the game purchase interface in the store
>   * Implement the backend logic to process purchases
>   * Test the entire purchase process to ensure it works correctly
> * **As a user, I would like to view the games that are in my library.**
>   * Configure the database to store information about the games in the user's library
>   * Create the interface to view the user's game library
>   * Develop the backend logic to manage the viewing of the game library
>   * Conduct tests to ensure the game library is displayed correctly
> * **As a user, I would like to start a game from my library.**
>   * Structure the database to store game installation information
>   * Develop the interface to start games from the library
>   * Implement the backend logic to enable game launching from the library
>   * Test and adjust the game launching process to ensure it works correctly
