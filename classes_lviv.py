"module with needed for the classes1 classes"

from classes1 import (Room, Enemy, Item)

class Supporter(Enemy):
    def __repr__(self):
        return self.name
