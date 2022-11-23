import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("TOKEN")
MY_TAG = os.getenv("PLAYER_TAG")

headers = {"authorization": "Bearer " + API_TOKEN, "Accept": "application/json"}


class Player:
    def __init__(self, tag, name, clan, level, trophies):
        self.tag = tag
        self.name = name
        self.clan = clan
        self.level = level
        self.trophies = trophies

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def clan(self):
        return self._clan

    @clan.setter
    def clan(self, value):
        self._clan = value

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value

    @property
    def trophies(self):
        return self._trophies

    @trophies.setter
    def trophies(self, value):
        self._trophies = value


class Clan:
    def __init__(self, tag, name, level, points, members):
        self.tag = tag
        self.name = name
        self.level = level
        self.points = points
        self.members = members

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def level(self):
        return self._level

    @level.setter
    def points(self, value):
        self._level = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    @property
    def members(self):
        return self._members

    @members.setter
    def members(self, value):
        self._members = value




all_players = []
all_clans = []

def add_player():
def search_clans():
    # clan search api
    response = requests.get(
        "https://api.clashofclans.com/v1/clans?name=new%20zealand%20gold",
        headers=headers,
    )
    clan = response.json()
    # now to go into items
    for clan in clan["items"]:
        print(clan["name"] + " is level: " + str(clan["clanLevel"]))


def get_stats():
    response = requests.get(
        "https://api.clashofclans.com/v1/players/%23" + MY_TAG, headers=headers
    )
    print(response.text)
    player = response.json()
    name = player["name"]
    print(f"{name}'s best trophies were " + str(player["bestTrophies"]))
