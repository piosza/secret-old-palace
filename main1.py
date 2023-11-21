import random
import json
import time


class Player:
    def __init__(self, name, health, money, wisdom):
        self.name = name
        self.health = health
        self.equipment = []
        self.money = money
        self.wisdom = wisdom

    def __str__(self):
        return (
            f"name: {self.name} health : {self.health}"
            f"money: {self.money} wisdom : {self.wisdom} "
        )

    def get_best_item(self):
        #        return sorted(self.equipment, key=lambda item: item.power, reverse=True)[0]
        return max(self.equipment, key=lambda item: item.power)

    def fight(self, monster):
        who_is_atacking = self
        who_is_defending = monster

        while self.health > 0 and monster.health > 0:
            fighting_weapon = who_is_atacking.get_best_item()
            print(f"{who_is_atacking.name}   you are fighting with   {fighting_weapon}")
            print(f" your turn {who_is_atacking.name} ")
            print(f" {self.name } your helth {self.health} ")
            print(f" {monster.name } your enemy helth {monster.health} ")
            random_extra_power = random.randint(-5, 5)
            sum_of_power = fighting_weapon.power + random_extra_power
            print(
                f"{self.name } you hit used {fighting_weapon.name} with power {fighting_weapon.power} with extra power {random_extra_power} sum of your attack {sum_of_power}"
            )
            who_is_defending.health -= sum_of_power
            print(
                f"{who_is_defending.name} after attack have {who_is_defending.health}"
            )
            #            time.sleep(2)
            input()
            if who_is_atacking == monster:
                who_is_atacking = self
            elif who_is_atacking == self:
                who_is_atacking = monster
            if who_is_defending == monster:
                who_is_defending = self
            elif who_is_defending == self:
                who_is_defending = monster

            #            print(f" your turn {who_is_atacking.monster.name} ")
            def death_of_monster():
                list_death_of_monster = [
                    "is dead and you can eat them",
                    "monster die",
                    "end of then",
                    "slashed",
                ]

                drawn_message = random.choice(list_death_of_monster)

                return drawn_message

            drawn_message_death = death_of_monster()

            if monster.health < 0:
                print(f"{monster.name }: {drawn_message_death} ")
            else:
                print(f"{monster.name } still alive ")


#            break


class Room:
    def __init__(
        self,
        room_number,
        monster_chance,
        merchant_chance,
        treasure_chance,
        nothing_chance,
        aviable_monster=list(),
    ):
        self.room_number = room_number
        self.chance_to_meet_monster = monster_chance
        self.chance_to_meet_merchant = merchant_chance
        self.chance_to_meet_tresure = treasure_chance
        self.chance_to_meet_nothing = nothing_chance
        self.aviable_monster = aviable_monster
        self.next_rooms = []
        self.room_decsrition = ""

    def __str__(self):
        return f" chamber : {self.room_number} "

    def show_allowed_rooms(self):
        print("next allowed rooms")
        for count, room in enumerate(self.next_rooms, start=1):
            print(count, room)

    def enter(self, player):
        print(f"{self.description}     \n  ############")
        #       if len(self.aviable_monster) > 0:
        #       if len(self.aviable_monster):
        if self.aviable_monster:
            print(f"you find monster : {self.aviable_monster}     \n  $$$$$$$$$$")
            #        for room in self.next_rooms:
            #            print(f"{room}")
            can_escape = True if random.randint(0, 100) > 50 else False
            # can_escape = random.randint(0, 100) > 50

            while True:
                event = input(" do you want figtht  F or escape E ")
                if event == "F" or event == "f":
                    player.fight(self.aviable_monster[0])
                    break

                elif event == "E" or event == "e":
                    if can_escape is False:
                        print("escape not allowed you must fight")
                    if can_escape is True:
                        print("first to escape you looser")
                    break
                else:
                    print(" <<<<<<<<<   wrong option   >>>>>>>>")

        self.show_allowed_rooms()

        while True:
            try:
                place = int(input(" give the number of the chamber you want to go to "))
                if place <= len(self.next_rooms) and place > 0:
                    break
                else:
                    print("wrong room")

                    self.show_allowed_rooms()
            except ValueError:
                print("This is not the correct chamber number. Try again")
                self.show_allowed_rooms()
        self.next_rooms[place - 1].enter(player)


class Weapon:
    def __init__(self, name, power, base_price, rarity):
        self.name = name
        self.power = power
        self.base_price = base_price
        self.rarity = rarity

    def __repr__(self):
        return f"weapon name: {self.name} power : {self.power}"

        # return f"{self.name=}"


class Merchant:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.equipment = []


class Monster:
    def __init__(self, name, health, power, money, equipment=list()):
        self.name = name
        self.health = health
        self.power = power
        self.money = money
        self.equipment = equipment

    def get_best_item(self):
        #        return sorted(self.equipment, key=lambda item: item.power, reverse=True)[0]
        return max(self.equipment, key=lambda item: item.power)

    def __repr__(self):
        return f"monster name: {self.name} health : {self.health} power: {self.power}, money :{self.money}:equipment : {self.equipment} "


def main():
    player = Player(
        input(" player name, type here o  -->  "),
        health=random.randint(1, 10),
        money=random.randint(1, 10),
        wisdom=random.randint(1, 10),
    )
    weapon = Weapon("fist", 5, 5, 1)
    player.equipment.append(weapon)
    weapon = Weapon("pipe", 1, 1, 1)
    player.equipment.append(weapon)
    weapon = Weapon("candle", 2, 2, 2)
    player.equipment.append(weapon)
    print(player)
    print(weapon)
    print(player.get_best_item())
    rooms = []
    comb_weapon = Weapon("comb", 0, 0, 1)
    rake_weapon = Weapon("rake", 1, 0, 1)

    monster_mati = Monster("Mati", 10, 5, 100000000, [comb_weapon])
    monster_donek = Monster("Donek", 50, 5, 100, [rake_weapon])
    print(monster_donek)

    rooms.append(Room("A1", 0.10, 0, 0, 1))

    def list_of_welcome_message():
        list_welcome_message = [
            "your trip begin ! young travelers",
            "bad choice it is very dangerous",
            "probably many problems, too many ",
            "you're scared very right ? ",
            "Be brave even though you will probably die anyway",
        ]

        welcom_message = random.choice(list_welcome_message)

        return welcom_message

    first_welcome_message = list_of_welcome_message()

    rooms[-1].description = f"{player.name }: {first_welcome_message} "
    rooms.append(Room("B1", 0.50, 0, 0, 1, [monster_donek]))
    rooms[-1].description = "room with fireplace"
    rooms.append(Room("B2", 0.50, 0, 0, 1))
    rooms[-1].description = "ugly room with chupacabra or not"
    rooms.append(Room("B3", 0.20, 0, 0, 1))
    rooms[-1].description = "devastaded  old room "
    rooms.append(Room("C1", 0.8, 0, 0, 1))
    rooms[-1].description = "dusty  old room  with ugly pictury on the wall"
    rooms.append(Room("C2", 0.8, 0, 0, 1))
    rooms[-1].description = "old room , with small window and animal skeleton"
    rooms.append(Room("C3", 0.8, 0, 0, 1))
    rooms[-1].description = "dusty  old room  with ugly pictury on the wall"
    rooms.append(Room("D1", 0.3, 0, 0, 1))
    rooms[
        -1
    ].description = "dusty  old room  with big ugly pictury on the wall,in the picture a sad old man"
    rooms.append(Room("D2", 0.6, 0, 0, 1))
    rooms[-1].description = "old destoyed room , with empty vine barrel"
    rooms.append(Room("D3", 0.3, 0, 0, 1))
    rooms[-1].description = "dusty  room  family chamber "
    rooms.append(Room("E1", 0.3, 0, 0, 1))
    rooms[
        -1
    ].description = "old room, last room on your trip , grating falls you die of thirst"
    rooms.append(Room("E2", 0.6, 0, 0, 1))
    rooms[-1].description = "Decorated room, remnants of bouquets, shabby furniture"
    rooms.append(Room("F1", 0.8, 0, 0, 1))
    rooms[-1].description = "Great room with sarcophagus, sculptures on the walls "
    for count, room in enumerate(rooms):
        print(count, room)
    # relacje
    rooms[0].next_rooms = [rooms[2]]

    rooms[1].next_rooms = [rooms[2], rooms[4]]
    rooms[2].next_rooms = [rooms[1], rooms[3]]
    rooms[3].next_rooms = [rooms[6]]

    rooms[4].next_rooms = [rooms[7]]
    rooms[5].next_rooms = [rooms[2], rooms[8]]
    rooms[6].next_rooms = [rooms[3], rooms[9]]

    rooms[7].next_rooms = [rooms[10]]
    rooms[8].next_rooms = [rooms[7], rooms[5], rooms[9]]
    rooms[9].next_rooms = [rooms[11]]

    rooms[10].next_rooms = []
    rooms[11].next_rooms = [rooms[12]]

    rooms[12].next_rooms = []

    plik = open("monter.json")
    list_of_monsters = json.load(plik)
    print(f"monster list  : {list_of_monsters}")
    plik.close()

    plik = open("merchant.json")
    list_of_merchant = json.load(plik)
    print(f"merchant list  : {list_of_merchant}")
    plik.close()
    print("*******************")
    print(random.choice(list_of_monsters))
    print(random.choice(list_of_merchant))
    rooms[0].enter(player)


if __name__ == "__main__":
    main()
