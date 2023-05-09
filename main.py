import sys
import time
from threading import Thread


class Animal:

    def __init__(self, food: int, water: int, entertainment: int, sleep: int, health: int):
        if 101 > food > 0:
            self.food = food
        if 101 > water > 0:
            self.water = water
        if 101 > entertainment > 0:
            self.entertainment = entertainment
        if 101 > sleep > 0:
            self.sleep = sleep
        if 101 > health > 0:
            self.health = health

    def time_work(self):
        self.food -= 20
        self.water -= 30
        self.entertainment -= 10
        self.sleep -= 20
        self.health -= 25
        if (self.sleep <= 0 or self.water <= 0 or self.entertainment <= 0 or self.sleep <= 0):
            self.health -= 40
            if self.health <= 0:
                print("fhfhfhfhfh")
                sys.exit("Health is over, your animal died")
            else:
                print(
                    f"Your parameters are:\nfood= {self.food},\twater= {self.water},\tentertainment= {self.entertainment}"
                    f",\tcheerful= {self.sleep},\thealth= {self.health}\nEach max value is 100")
        else:
            print(f"Your parameters are:\nfood= {self.food},\twater= {self.water},\tentertainment= {self.entertainment}"
                  f",\tcheerful= {self.sleep},\thealth= {self.health}\nEach max value is 100")
        return self.food, self.water, self.entertainment, self.sleep, self.health

    def level_food(self):
        self.food += 10
        if self.food >= 100:
            self.health -= 30
            if self.health <= 0:
                sys.exit("Health is over, your animal died")
        elif self.food <= 0:
            self.health -= 40
        print("Your levels food=", self.food, "and health=", self.health)
        return self.food, self.health

    def level_water(self):
        self.water += 10
        if self.water >= 100:
            self.health -= 30
            if self.health <= 0:
                sys.exit("Health is over, your animal died")
        elif self.water <= 0:
            self.health -= 40
        print("Your levels water=", self.water, "and health=", self.health)
        return self.water, self.health

    def level_entertainment(self):
        self.entertainment += 10
        if self.entertainment >= 100:
            self.health -= 30
            if self.health <= 0:
                sys.exit("Health is over, your animal died")
        elif self.entertainment <= 0:
            self.health -= 40
        print("Your levels funny=", self.entertainment, "and health=", self.health)
        return self.entertainment, self.health

    def level_sleep(self):
        self.sleep += 10
        if self.sleep >= 100:
            self.health -= 30
            if self.health <= 0:
                sys.exit("Health is over, your animal died")
        elif self.sleep <= 0:
            self.health -= 40
        print("Your levels tired=", self.sleep, "and health=", self.health)
        return self.sleep, self.health

    def start_play(self):
        while True:
            print(f"Your parameters are:\nfood= {self.food},\twater= {self.water},\tentertainment= {self.entertainment}"
                  f",\tcheerful= {self.sleep},\thealth= {self.health}\nEach max value is 100")

            answer = input("Hello, what do you want to do with your pet\n\tfeed\n\tgive to drink\n\tentertain\n\tsleep"
                           "\nFor exit write exit\nPlease write here:").lower()

            match answer:
                case "feed":
                    Animal.level_food(self)
                case "give to drink":
                    Animal.level_water(self)
                case "entertain":
                    Animal.level_entertainment(self)
                case "sleep":
                    Animal.level_sleep(self)
                case "exit":
                    break
                case _:
                    print("Please write from topic")
        return


def add_data(level_foods, level_waters, level_entertainments, level_sleeps, level_healths):
    try:
        user = Animal(level_foods, level_waters, level_entertainments, level_sleeps, level_healths)
        th1 = Thread(target=user.start_play)
        th1.start()
        while True:
            time.sleep(1)
            user.time_work()
            if user.start_play == False:
                break
    except: return "error please check your data"


add_data(70, 80, 50, 60, 10)

# user = Animal(55, 80, 60, 70, 40)
# th1 = Thread(target=user.start_play)
# th1.start()
# while True:
#     time.sleep(2)
#     user.time_work()
#     if user.start_play == False:
#         break