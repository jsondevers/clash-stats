import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("TOKEN")
MY_TAG = os.getenv("PLAYER_TAG")

headers = {"authorization": "Bearer " + API_TOKEN, "Accept": "application/json"}


# class Player:
#     def __init__(self, tag, name, clan, level, trophies):
#         self.tag = tag
#         self.name = name
#         self.clan = clan
#         self.level = level
#         self.trophies = trophies

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     def name(self, value):
#         self._name = value


def get_stats():
    response = requests.get(
        "https://api.clashofclans.com/v1/players/%23" + MY_TAG, headers=headers
    )
    print(response.text)
    player = response.json()
    name = player["name"]
    print(f"{name}'s best trophies were " + str(player["bestTrophies"]))


get_stats()
# class Clan:
#     def search_clans():
#         # clan search api
#         response = requests.get(
#             "https://api.clashofclans.com/v1/clans?name=new%20zealand%20gold",
#             headers=headers,
#         )
#         clan = response.json()
#         # now to go into items
#         for clan in clan["items"]:
#             print(clan["name"] + " is level: " + str(clan["clanLevel"]))


# # # these functions will be called
# get_player()
# # search_clans()
