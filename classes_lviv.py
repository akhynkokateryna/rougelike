"Classes for the second game - rougelike in Lviv"

from classes1 import (Room, Enemy, Item)


class Player:
    "Represents some features for the main player"
    def __init__(self, name):
        self.name = name
        self.backpack = []
        self.supporters = []


class Supporter(Enemy):
    def __str__(self):
        return self.name
