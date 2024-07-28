from threading import Thread
import requests
import time
from time import sleep

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0


    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies != 0:
            self.enemies = self.enemies - self.power
            self.days = self.days + 1
            time.sleep(1)
            print(f'{self.name} сражается {self.days} дней(дня), осталось {self.enemies} воинов.')

        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')

threads = []

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

for thread in threads:
    thread.join()
