import requests
import json
from gitcolors import Gitcolors as gc

API_MAIN_URL = 'https://api.github.com/'
API_REPO_URL = 'https://api.github.com/users/user/repos'

class RepoList:
    def __init__(self, user):
        self._user = user

    def requestApi(self):
        response = requests.get(f"https://api.github.com/users/{self._user}/repos")

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def listRepos(self):
        API_DATA     = self.requestApi()
        API_DATA_LEN = len(API_DATA)

        REPO_NUM = 1;

        if type(API_DATA) is not int:
            for i in range(API_DATA_LEN):
                print(f"{gc.white}Repository nº {REPO_NUM}{gc.res} - {gc.yellow}{API_DATA[i]['name']}{gc.res}")

                REPO_NUM += 1
        else:
            print(API_DATA)

