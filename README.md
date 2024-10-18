# Gerenciador de Seguidores do GitHub

Este projeto é um script Python que interage com a API do GitHub para gerenciar seus seguidores e as pessoas que você está seguindo. Ele permite que você siga automaticamente novos seguidores e pare de seguir aqueles que não o seguem mais.

## Funcionalidades

- **Obter todos os seguidores**: Recupera uma lista de todos os seguidores do usuário especificado.
- **Obter quem você está seguindo**: Recupera uma lista de usuários que você está seguindo.
- **Seguir usuários automaticamente**: Segue automaticamente novos seguidores que não estão na sua lista de seguidos.
- **Deixar de seguir usuários**: Para de seguir aqueles que não o seguem mais.
- **Salvar resultados**: Salva os usuários que você começou a seguir e aqueles que você deixou de seguir em arquivos JSON.

## Pré-requisitos

- Python 3.x
- Bibliotecas: `requests`, `python-dotenv`

## Instalação

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_DIRETORIO>
   ```

2. Instale as dependências:

    ```
    pip install requests python-dotenv
    ```

3. Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais do GitHub:

    ```
    GITHUB_TOKEN=seu_token_do_github
    USER_NAME=seu_nome_de_usuario
    ```

- Para obter um GITHUB_TOKEN, siga as instruções na documentação do GitHub.

# Uso

- Para executar o script, use o seguinte comando:

    ```
    python gerenciador_seguidores.py
    ```

# Saída

- O script salvará dois arquivos JSON:
  - `followed_users.json:` Lista de usuários que você começou a seguir.
  - `unfollowed_users.json:` Lista de usuários que você deixou de seguir.

# Contribuição

Sinta-se à vontade para contribuir com melhorias ou relatar problemas. Para contribuir:

- Faça um fork do projeto.
- Crie uma nova branch (`git checkout -b feature/NovaFuncionalidade`).
- Faça suas alterações e commit (`git commit -m 'Adicionando nova funcionalidade'`).
- Envie para o repositório remoto (`git push origin feature/NovaFuncionalidade`).
- Abra um Pull Request.

# Licença

Este projeto está licenciado sob a Licença MIT.

### Personalizações

- Certifique-se de substituir `<URL_DO_REPOSITORIO>` e `<NOME_DO_DIRETORIO>` pelos valores apropriados.
- Se você tiver uma licença específica, adicione-a ao repositório e altere a seção de licença conforme necessário.

Sinta-se à vontade para modificar o README conforme suas necessidades!


# GitHub Followers Manager

This project is a Python script that interacts with the GitHub API to manage your followers and the people you are following. It allows you to automatically follow new followers and unfollow those who no longer follow you.

## Features

- **Get all followers**: Retrieves a list of all the followers of the specified user.
- **Get who you are following**: Retrieves a list of users you are currently following.
- **Automatically follow users**: Automatically follows new followers who are not on your following list.
- **Unfollow users**: Unfollows users who no longer follow you.
- **Save results**: Saves the users you started following and those you unfollowed in JSON files.

## Requirements

- Python 3.x
- Libraries: `requests`, `python-dotenv`

## Installation

1. Clone the repository:

   ```bash
   git clone <REPOSITORY_URL>
   cd <DIRECTORY_NAME>
    ```


2. Install the dependencies:

    ```
    pip install requests python-dotenv
    ```

3. Create a `.env` file in the project root and add your GitHub credentials:

    ```
    GITHUB_TOKEN=your_github_token
    USER_NAME=your_github_username
    ```

- To get a GITHUB_TOKEN, follow the instructions in the GitHub documentation.

# Usage

- To run the script, use the following command:

    ```
    python gerenciador_seguidores.py
    ```

# Output

- The script will save two JSON files:
    - `followed_users.json`: A list of users you started following.
    - `unfollowed_users.json`: A list of users you unfollowed.

# Contribution

Feel free to contribute with improvements or report any issues. To contribute:

- Fork the project.
- Create a new branch (`git checkout -b feature/NewFeature`).
- Make your changes and commit (`git commit -m 'Adding new feature'`).
- Push to the remote repository (`git push origin feature/NewFeature`).
- Open a Pull Request.

# License

This project is licensed under the MIT License.

## Customizations

- Be sure to replace `<REPOSITORY_URL>` and `<DIRECTORY_NAME>` with the appropriate values.
- If you have a specific license, add it to the repository and modify the license section as necessary.

Feel free to modify the README as needed!

Let me know if you need any further adjustments!
