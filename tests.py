import unittest
from clash import Player, Clan, Manager


class TestPlayer(unittest.TestCase):
    def player_equals(self):
        p1 = Player(tag="test", name="player1")
        p2 = Player(tag="test", name="player2")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())


class TestClan(unittest.TestCase):
    def player_equals(self):
        c1 = Clan(tag="test", name="player1")
        c2 = Clan(tag="test", name="player2")


class TestManager(unittest.TestCase):
    def find_clan(self):
        m1 = Manager({}, {})

    def find_player(self):
        p1 = Player(tag="test", name="player1")
        p2 = Player(tag="test", name="player2")


if __name__ == "__main__":
    unittest.main()
