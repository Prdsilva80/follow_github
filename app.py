import requests
import os
import json
from dotenv import load_dotenv
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Carregar token do .env
load_dotenv()
TOKEN = os.getenv('GITHUB_TOKEN')
USERNAME = os.getenv('USER_NAME')

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Lista de usuários bloqueados
BLOCKED_USERS = os.getenv('BLOCKED_USERS')

# Função genérica para obter dados paginados
def get_paginated_data(url):
    data = []
    page = 1
    while True:
        try:
            response = requests.get(f"{url}?page={page}&per_page=100", headers=HEADERS)
            response.raise_for_status()
            page_data = response.json()
            if not page_data:
                break
            data.extend(page_data)
            page += 1
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro ao obter dados: {e}")
            break
    return data

# Função para obter todos os seguidores
def get_followers():
    url = f"https://api.github.com/users/{USERNAME}/followers"
    followers = get_paginated_data(url)
    return [follower['login'] for follower in followers]

# Função para obter quem você está seguindo
def get_following():
    url = f"https://api.github.com/users/{USERNAME}/following"
    following = get_paginated_data(url)
    return [user['login'] for user in following]

# Função para seguir usuários
def follow_user(user):
    if user in BLOCKED_USERS:
        logging.info(f"Usuário {user} está bloqueado e não será seguido.")
        return False
    url = f"https://api.github.com/user/following/{user}"
    try:
        response = requests.put(url, headers=HEADERS)
        response.raise_for_status()
        if response.status_code == 204:
            logging.info(f"Agora você está seguindo {user}")
            return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Falha ao seguir {user}. Erro: {e}")
    return False

# Função para deixar de seguir usuários
def unfollow_user(user):
    url = f"https://api.github.com/user/following/{user}"
    try:
        response = requests.delete(url, headers=HEADERS)
        response.raise_for_status()
        if response.status_code == 204:
            logging.info(f"Parou de seguir {user}")
            return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Falha ao parar de seguir {user}. Erro: {e}")
    return False

# Função para bloquear usuários
def block_user(user):
    url = f"https://api.github.com/user/blocks/{user}"
    try:
        response = requests.put(url, headers=HEADERS)
        response.raise_for_status()
        if response.status_code == 204:
            logging.info(f"Usuário {user} foi bloqueado")
            return True
    except requests.exceptions.RequestException as e:
        logging.error(f"Falha ao bloquear {user}. Erro: {e}")
    return False

# Função para salvar dados em JSON
def save_to_json(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Função principal para gerenciar seguidores e seguidos
def manage_following():
    current_followers = get_followers()
    following = get_following()

    unfollowed_users = []
    followed_users = []

    # Listas para investigar diferenças
    not_following_back = [user for user in following if user not in current_followers]
    not_followed_by_me = [user for user in current_followers if user not in following]

    # Exibe os resultados
    if not_following_back:
        logging.info("Usuários que você segue mas não te seguem de volta: %s", not_following_back)
    else:
        logging.info("Todos que você segue também te seguem de volta.")

    if not_followed_by_me:
        logging.info("Usuários que te seguem mas você não segue de volta: %s", not_followed_by_me)
    else:
        logging.info("Você segue todos os seus seguidores.")

    # Parar de seguir quem não te segue de volta
    for user in not_following_back:
        if unfollow_user(user):
            unfollowed_users.append(user)

    # Seguir automaticamente quem te segue, mas você não segue
    for user in not_followed_by_me:
        if follow_user(user):
            followed_users.append(user)

    # Deixar de seguir e bloquear usuários bloqueados
    for user in BLOCKED_USERS:
        if user in following:
            if unfollow_user(user):
                unfollowed_users.append(user)
        if user in current_followers:
            if block_user(user):
                logging.info(f"Usuário {user} foi removido da lista de seguidores")

    # Salvar os resultados em arquivos JSON
    save_to_json("unfollowed_users.json", unfollowed_users)
    save_to_json("followed_users.json", followed_users)

if __name__ == "__main__":
    manage_following()