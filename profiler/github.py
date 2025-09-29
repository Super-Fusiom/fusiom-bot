import requests


class GithubUser:
    def __init__(self, username: str):
        self._api_url = f"https://api.github.com/users/{username}"
        self.username = username
        self._repos: dict
        self._followers: dict
        self.__fetch_repos()
        self.__fetch_followers()

    @property
    def repos(self):
        return self._repos

    @property
    def followers(self):
        return self._followers

    def __fetch_repos(self):
        api_url = f"{self._api_url}/repos"
        response = requests.get(api_url)
        data = response.json()
        self._repos = data

    def __fetch_followers(self):
        api_url = f"{self._api_url}/followers"
        response = requests.get(api_url)
        data = response.json()
        self._followers = data

    def __str__(self):        
        return f"{self.username} has {len(self._repos)} repos"


def fetch_github_repos(username: str):
    spied = GithubUser(username)
    return f"This {spied.username} has {len(spied.repos)} repos"

def fetch_github_all(username: str):
    spied = GithubUser(username)
    return f"This {spied.username} has {len(spied.repos)} repos and {len(spied.followers)} followers"