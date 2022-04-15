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

Taras = classes_lviv.Supporter("Taras", "A nice kavaler that will be accompany you and protect when necessary.")
Taras.set_conversation("Oaoaoa, what a princess is coming. Bizhenciv ne pryimayete?")
franka.set_character(Taras)

nalyvka = classes_lviv.Item("nalyvka")
nalyvka.set_description("Powerful tool :)")
stryiska.set_item(nalyvka)

Andriy = classes_lviv.Enemy("Andriy", "An alcoholic without priorities")
Andriy.set_conversation("A bottle of nalyvka and you can go.")
Andriy.set_weakness("nalyvka")
krakivska.set_character(Andriy)

Ivan = classes_lviv.Enemy("Ivan", "An usnstoppable batyar (only kavaler can save you from him)")
Ivan.set_conversation("Only another ambitious man can defeat me.")
Ivan.set_weakness(Taras)
shevchenka.set_character(Ivan)

Serhiy = classes_lviv.Enemy("Serhiy", "A robber")
Serhiy.set_conversation("Hello, hello.. Only a student can stop me (students don't have any fears)")
Serhiy.set_weakness(Bodya)
stryiska.set_character(Serhiy)

food = classes_lviv.Item("food")
food.set_description("Just food, students don't care about what exactly that is anyway.")
kozelnytska.set_item(food)


current_street = kozelnytska
current_street_counter_k = 1
current_street_counter_kr = 0


dead = False

new_name = input("Enter your character's name: ")
player = classes_lviv.Player(new_name)

while dead is False:

    print("\n")
    print("Possible actions: direction, talk, fight, take, get support, see backpack, see supporters.",\
        "Enter 'exit' if you want to end the game.", sep="\n")
    print("\n")
    current_street.get_details()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_street.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_street = current_street.move(command)
        if current_street.name == "Kozelnytska":
            current_street_counter_k += 1
        elif current_street.name == "Krakivska":
            current_street_counter_kr += 1

        if current_street_counter_k == 2 and current_street_counter_kr >= 1:
            print("You have successfully finished your trip!")
            dead = True

    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()

    elif command == "fight":
        if isinstance(inhabitant, classes_lviv.Supporter):
            print(f"{str(current_street.get_character())} can be your supporter")

        elif inhabitant is None:
            print("There is no one here to fight with")

        else:
            if isinstance(inhabitant.weakness, classes_lviv.Supporter):
                print("Which supporter will help you?")
                fight_with_sup = input()
                for sup in player.supporters:
                    if sup.name == fight_with_sup:
                        if inhabitant.fight(sup) is True:
                            print("Hooray, you won the fight!")
                            current_street.character = None
                        else:
                            print("Oh dear, you lost the fight.", "That's the end of the game", sep="\n")
                            dead = True

            else:
                print("What will you fight with?")
                fight_with = input()

                if fight_with in player.backpack:

                    if inhabitant.weakness == fight_with:
                        print("Hooray, you won the fight!")
                        current_street.character = None
                    else:
                        print("Oh dear, you lost the fight.", "That's the end of the game", sep="\n")
                        dead = True
                else:
                    print("You don't have a " + fight_with)

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            player.backpack.append(item.get_name())
            current_street.item = None
        else:
            print("There's nothing here to take!")

    elif command == "get support":
        if current_street.get_character() is Bodya:
            try:
                player.backpack.remove("food")
            except ValueError:
                print("You don't have food in your backpack to give it to Bodya and get his support")
                continue
            print("To have Bodya as a supporter u gave him your food")
        player.supporters.append(current_street.get_character())
        current_street.character = None
        print(f"Now {str(current_street.get_character())} will help u when u need")

    elif command == "see backpack":
        if len(player.backpack) == 0:
            print("Backpack is empty!")
        else:
            print(player.backpack)

    elif command == "see supporters":
        if len(player.supporters) == 0:
            print("You don't have supporters yet!")
        else:
            print([str(x) for x in player.supporters])

    elif command == "exit":
        print("Thanks for the game!")
        dead = True

    else:
        print("No such command!")
