import requests
import json
from gitcolors import Gitcolors as gc

API_USER_URL = 'https://api.github.com/users/user/'

class UserData:
    def __init__(self, user : str) -> None:
        self.user = user

    def requestApi(self) -> None:
        response = requests.get(f"https://api.github.com/users/{self.user}")

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def ShowData(self) -> None:
        API_DATA = self.requestApi()
       # API_LEN  = len(API_DATA)

        if type(API_DATA) is not int:
            LOGIN       = API_DATA["login"]
            NAME        = API_DATA["name"]
            LOCATION    = API_DATA["location"]
            BIO         = API_DATA["bio"]
            FOLLOWERS   = API_DATA["followers"]
            FOLLOWING   = API_DATA["following"]
            PUBLIC_REPS = API_DATA["public_repos"]

            print(f"{gc.white}[🐍] Login       {gc.res} - {gc.yellow}{LOGIN}")
            print(f"{gc.white}[🍕] Name        {gc.res} - {gc.yellow}{NAME}")
            print(f"{gc.white}[📌] Location    {gc.res} - {gc.yellow}{LOCATION}")
            print(f"{gc.white}[📗] Bio         {gc.res} - {gc.yellow}{BIO}")
            print(f"{gc.white}[↙️] Followers   {gc.res} - {gc.yellow}{FOLLOWERS}")
            print(f"{gc.white}[↗️] Following   {gc.res} - {gc.yellow}{FOLLOWING}")
            print(f"{gc.white}[☂️] Public repos{gc.res} - {gc.yellow}{PUBLIC_REPS}")

        else:
            print(API_DATA)
