import requests


class GithubUser:
    def __init__(self, username: str):
        self._username = username


def fetch_github_user(username: str):
    api_url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(api_url)
    data = response.json()
    out = ""
    num_of_repos = len(data)
    if num_of_repos < 10:
        out += f"This {username} is a donkey with {num_of_repos} repos"
    else:
        out += f"This {username} is a genius with {num_of_repos} repos"
    return out
