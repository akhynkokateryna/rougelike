"Classes for the first game"


class Room:
    "Represents a room in the first game and a street in the other"

    def __init__(self, name):
        self.name = name
        self.character = None
        self.item = None
        self.descrip = ""
        self.linked_rooms = []

    def set_description(self, descr):
        "Sets description for the room/street"
        self.descrip = descr

    def link_room(self, room, direction):
        "Adds directions for other rooms/streets from the current room/street"
        self.linked_rooms.append((room, direction))

    def set_character(self, char):
        "Adds character to the room/street"
        self.character = char

    def set_item(self, new_item):
        "Adds item for the room/street"
        self.item = new_item

    def get_details(self):
        "Shows info about the room/street"
        print(self.name)
        print("- - - - - - - - - - - - -")
        print(self.descrip)
        for room in self.linked_rooms:
            print(f"The {room[0]} is {room[1]}")

    def get_character(self):
        "Returns character that is in the current room/street"
        return self.character

    def get_item(self):
        "Returns item that is in the current room/street"
        if self.item is None:
            return None
        else:
            return self.item

    def move(self, direct):
        "Changes current room/street to the room/street in entered direction"
        for link_room in self.linked_rooms:
            if link_room[1] == direct:
                return link_room[0]

    def __repr__(self):
        return self.name


class Enemy:
    "Represents characters"

    dead_enemies = 0

    def __init__(self, name, descr):
        self.name = name
        self.descr = descr
        self.weakness = None
        self.conversation = ""

    def set_conversation(self, message):
        "Sets conversation for the character"
        self.conversation = message

    def set_weakness(self, weakness):
        "Sets weakness for the character"
        self.weakness = weakness

    def describe(self):
        "Prints info about the character"
        print(f"{self.name} is here!", self.descr, sep="\n")

    def talk(self):
        "Prints character's phrase"
        print(f"[{self.name} says]: {self.conversation}")

    def get_defeated(self):
        "Adds num to the num of dead enemies and returns the current num of them"
        self.dead_enemies += 1
        return self.dead_enemies

    def fight(self, weapon):
        "Returns True if enemy can be defeated with that item"
        if weapon is self.weakness:
            return True


class Item:
    "Represents items"

    def __init__(self, name):
        self.name = name
        self.descrip = None

    def set_description(self, descr):
        "Sets description for the item"
        self.descrip = descr

    def describe(self):
        "Prints description for the item"
        print(f"The [{self.name}] is here - {self.descrip}")

    def get_name(self):
        "returns item's name"
        return self.name

    def __repr__(self):
        return self.name
