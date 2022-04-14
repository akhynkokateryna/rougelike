"main_lviv.py"

import classes_lviv


kozelnytska = classes_lviv.Room("Kozelnytska")
kozelnytska.set_description("Cool street with cool campus.")

stryiska = classes_lviv.Room("Stryiska")
stryiska.set_description("One of the longest streets that ends with (almost) Russia supporter (Auchan).")

franka = classes_lviv.Room("Franka")
franka.set_description("Two-in-one: park on the one hand, nice architecture on the other.")

shevchenka = classes_lviv.Room("Shevchenka")
shevchenka.set_description("Visit oceanarium, eat in Pusata Hata, and see Hrushevskyi Monument.")

krakivska = classes_lviv.Room("Krakivska")
krakivska.set_description("Maaaany different bars and museums.")

kozelnytska.link_room(stryiska, 'west')
kozelnytska.link_room(franka, 'north')
stryiska.link_room(kozelnytska, 'east')
stryiska.link_room(franka, 'north')
stryiska.link_room(shevchenka, 'west')
franka.link_room(kozelnytska, 'south')
franka.link_room(stryiska, 'west')
shevchenka.link_room(stryiska, 'east')
shevchenka.link_room(krakivska, 'north')
krakivska.link_room(shevchenka, 'south')

Bodya = classes_lviv.Supporter("Bodya", "A smelly zombie-student that does everything for food (give him it and he might help you in future :))")
Bodya.set_conversation("What's up, dude! I'm hungry.")
Bodya.set_weakness("food")
kozelnytska.set_character(Bodya)

Hryhoriy = classes_lviv.Supporter("Hryhoriy", "A nice kavaler that will be accompany you and protect when necessary.")
Hryhoriy.set_conversation("Oaoaoa, what a princess is coming. Bizhenciv ne pryimayete?")
franka.set_character(Hryhoriy)

Andriy = classes_lviv.Enemy("Andriy", "An alcoholic without priorities")
Andriy.set_conversation("A bottle of horilka and you can go.")
Andriy.set_weakness("horilka")
krakivska.set_character(Andriy)

Ivan = classes_lviv.Enemy("Ivan", "An usnstoppable batyar (only kavaler can save you from him)")
Ivan.set_conversation("Only another ambitious man can defeat me.")
Ivan.set_weakness("Hryhoriy")
shevchenka.set_character(Ivan)

Serhiy = classes_lviv.Enemy("Serhiy", "A robber")
Serhiy.set_conversation("Hello, hello.. Only a student can stop me (students don't have any fears)")
Serhiy.set_weakness("Bodya")
stryiska.set_character(Serhiy)

food = classes_lviv.Item("food")
food.set_description("Just food, students don't care about what exactly that is anyway.")
kozelnytska.set_item(food)

horilka = classes_lviv.Item("horilka")
horilka.set_description("Powerful tool :)")
stryiska.set_item(horilka)

current_room = kozelnytska
current_room_counter_k = 1
current_room_counter_kr = 0

backpack = []

dead = False

while dead == False:

    print("\n")
    print("Possible actions: direction, talk, fight, take, support")
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_room = current_room.move(command)
        if current_room == "kozelnytska":
            current_room_counter_k += 1
        elif current_room == "krakivska":
            current_room_counter_kr += 1

        if current_room_counter_k == 2 and current_room_counter_kr >= 1:
            print("You have successfully finished your trip!")
            dead = True

    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        if inhabitant is not None:
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")

    elif command == "support":
        print(f"Now {current_room.get_character()} is in your arsenal")

    elif command == "exit":
        print("Thanks for the game!")
        dead = True

    else:
        print("No such command!")
