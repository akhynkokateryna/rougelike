"Classes for the second game - rougelike in Lviv"

from classes1 import (Room, Enemy, Item)

class Supporter(Enemy):
    def __repr__(self):
        return self.name
