import random


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


class Room:
    def __init__(
        self,
        room_number,
        monster_chance,
        merchant_chance,
        treasure_chance,
        nothing_chance,
    ):
        self.room_number = room_number
        self.chance_to_meet_monster = monster_chance
        self.chance_to_meet_merchant = merchant_chance
        self.chance_to_meet_tresure = treasure_chance
        self.chance_to_meet_nothing = nothing_chance
        self.next_rooms = []
        self.room_decsrition = ""

    def __str__(self):
        return f" chamber : {self.room_number} "

    def enter(self):
        print(f"{self.description}     \n  rooms allowed")

        #        for room in self.next_rooms:
        #            print(f"{room}")
        for count, room in enumerate(self.next_rooms, start=1):
            print(count, room)

        while True:
            try:
                place = int(input(" give the number of the chamber you want to go to "))
                if place <= len(self.next_rooms) and place > 0:
                    break
                else:
                    print("wrong room")
            except ValueError:
                print("This is not the correct chamber number. Try again")

        self.next_rooms[place - 1].enter()


class Weapon:
    def __init__(self, power, name, base_price, rarity):
        self.powar = power
        self.name = name
        self.base_price = base_price
        self.rarity = rarity


class Merchant:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.equipment = []


class Monster:
    def __init__(self, name, health, money):
        self.name = name
        self.health = health
        self.money = money
        self.equipment = []


def main():
    player = Player(
        input(" player name, type here o  -->  "),
        health=random.randint(1, 10),
        money=random.randint(1, 10),
        wisdom=random.randint(1, 10),
    )

    print(player)
    rooms = []

    rooms.append(Room("A1", 0.10, 0, 0, 1))
    rooms[-1].description = "your trip begin ! young travelers"
    rooms.append(Room("B1", 0.50, 0, 0, 1))
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
    rooms[0].enter()


if __name__ == "__main__":
    main()
