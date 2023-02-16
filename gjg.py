import sys
import time
from threading import Thread


class Animal:

    def __init__(self, food, water, entertainment, sleep, health):
        self.food = food
        self.water = water
        self.entertainment = entertainment
        self.sleep = sleep
        self.health = health

    def time_work(self):
        self.food -= 20
        self.water -= 30
        self.entertainment -= 10
        self.sleep -= 20
        self.health -= 25
        if (self.sleep <= 0 or self.water <= 0 or self.entertainment <= 0 or self.sleep <= 0 or self.health <= 0):
            sys.exit("Health is over, your animal died")
        else:
            print(f"Your parameters are:\nfood= {self.food},\twater= {self.water},\tentertainment= {self.entertainment}"
                    f",\tcheerful= {self.sleep},\thealth= {self.health}\nEach max value is 100")


    def start_play(self):

        while True:
            print(f"Your parameters are:\nfood= {self.food},\twater= {self.water},\tentertainment= {self.entertainment}"
                  f",\tcheerful= {self.sleep},\thealth= {self.health}\nEach max value is 100")

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
                return self.water, self.health
            answer = input("Hello, what do you want to do with your pet\n\tfeed\n\tgive to drink\n\tentertain\n\tsleep"
                           "\nFor exit write exit\nPlease write here:").lower()

            match answer:
                case "feed":
                    level_food(self)
                case "give to drink":
                    level_water(self)
                case "entertain":
                    level_entertainment(self)
                case "sleep":
                    level_sleep(self)
                case "exit":
                    break
                case _:
                    print("Please write from topic")


user = Animal(70, 70, 70, 70, 70)
th1 = Thread(target=user.start_play)
th1.start()
while True:
    time.sleep(2)
    user.time_work()
    if user.start_play == False:
        break
