import requests
import os
import json
from dotenv import load_dotenv

# Carregar token do .env
load_dotenv()
TOKEN = os.getenv('GITHUB_TOKEN')
USERNAME = os.getenv('USER_NAME')

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Função para obter todos os seguidores com paginação
def get_followers():
    followers = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{USERNAME}/followers?page={page}&per_page=100"
        response = requests.get(url, headers=HEADERS)
        data = response.json()
        if len(data) == 0:
            break
        followers.extend([follower['login'] for follower in data])
        page += 1
    return followers

# Função para obter quem você está seguindo com paginação
def get_following():
    following = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{USERNAME}/following?page={page}&per_page=100"
        response = requests.get(url, headers=HEADERS)
        data = response.json()
        if len(data) == 0:
            break
        following.extend([following['login'] for following in data])
        page += 1
    return following

# Função para seguir usuários
def follow_user(user):
    url = f"https://api.github.com/user/following/{user}"
    response = requests.put(url, headers=HEADERS)
    if response.status_code == 204:
        print(f"Seguindo {user}")
        return True
    elif response.status_code == 404:
        print(f"Usuário {user} não encontrado. Código de erro: {response.status_code}")
    else:
        print(f"Falha ao seguir {user}. Código de erro: {response.status_code}")
    return False

# Função para deixar de seguir usuários
def unfollow_user(user):
    url = f"https://api.github.com/user/following/{user}"
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 204:
        print(f"Parou de seguir {user}")
        return True
    else:
        print(f"Falha ao parar de seguir {user}. Código de erro: {response.status_code}")
    return False

# Função para salvar dados em JSON
def save_to_json(filename, data):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Função principal para gerenciar seguidores
def manage_followers():
    current_followers = get_followers()
    following = get_following()

    followed_users = []
    unfollowed_users = []

    # Seguir automaticamente novos seguidores
    for follower in current_followers:
        if follower not in following:
            if follow_user(follower):
                followed_users.append(follower)

    # Parar de seguir quem deixou de te seguir
    for user in following:
        if user not in current_followers:
            if unfollow_user(user):
                unfollowed_users.append(user)

    # Salvar os resultados em arquivos JSON
    save_to_json("followed_users.json", followed_users)
    save_to_json("unfollowed_users.json", unfollowed_users)

if __name__ == "__main__":
    manage_followers()