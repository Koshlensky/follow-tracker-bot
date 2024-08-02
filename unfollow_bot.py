import requests
from github import Github

# Ваш GitHub токен
TOKEN = "ваш_токен"

# Создаем объект GitHub
g = Github(TOKEN)

# Ваше имя пользователя
USERNAME = "имя_пользователя"

# Получаем текущего пользователя
user = g.get_user(USERNAME)

# Получаем списки подписчиков и подписок
followers = user.get_followers()
following = user.get_following()

# Преобразуем в списки имен пользователей
followers_list = [follower.login for follower in followers]
following_list = [followed.login for followed in following]

# Ищем тех, кто отписался
unfollowed = [followed for followed in following_list if followed not in followers_list]

# URL для отписки от пользователя
UNFOLLOW_URL = "https://api.github.com/user/following/"

# Отписываемся от тех, кто отписался от вас
for unfollowed_user in unfollowed:
    response = requests.delete(
        UNFOLLOW_URL + unfollowed_user,
        headers={'Authorization': f'token {TOKEN}'}
    )
    if response.status_code == 204:
        print(f"Отписались от {unfollowed_user}")
    else:
        print(f"Не удалось отписаться от {unfollowed_user}: {response.status_code} {response.reason}")

print("Процесс завершен.")