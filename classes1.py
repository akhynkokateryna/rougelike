class Room:
    def __init__(self, name):
        self.name = name
        self.character = None
        self.item = None
        self.descrip = ""
        self.linked_rooms = []

    def set_description(self, descr):
        self.descrip = descr

    def link_room(self, room, direction):
        self.linked_rooms.append((room, direction))

    def set_character(self, char):
        self.character = char

    def set_item(self, new_item):
        self.item = new_item

    def get_details(self):
        print(self.name)
        print("- - - - - - - - - - - - -")
        print(self.descrip)
        for room in self.linked_rooms:
            print(f"The {room[0]} is {room[1]}")

    def get_character(self):
        return self.character

    def get_item(self):
        if self.item is None:
            return None
        else:
            return self.item

    def move(self, direct):
        for link_room in self.linked_rooms:
            if link_room[1] == direct:
                return link_room[0]

    def __repr__(self):
        return self.name


class Enemy:

    dead_enemies = 0

    def __init__(self, name, descr):
        self.name = name
        self.descr = descr
        self.weakness = None
        self.conversation = ""

    def set_conversation(self, message):
        self.conversation = message

    def set_weakness(self, weakness):
        self.weakness = weakness

    def describe(self):
        print(f"{self.name} is here!", self.descr, sep="\n")

    def talk(self):
        print(f"[{self.name} says]: {self.conversation}")

    def get_defeated(self):
        self.dead_enemies += 1
        return self.dead_enemies

    def fight(self, weapon):
        if weapon in self.weakness:
            return True


class Item:
    def __init__(self, name):
        self.name = name
        self.descrip = None

    def set_description(self, descr):
        self.descrip = descr

    def describe(self):
        print(f"The [{self.name}] is here - {self.descrip}")

    def get_name(self):
        return self.name

    def __repr__(self):
        return self.name
