import requests


class GithubUser:
    def __init__(self, username):
        self.username = username


def fetch_github_user(username):
    api_url = f"https://api.github.com/users/{username}"
    response = requests.get(api_url)
    response.json()