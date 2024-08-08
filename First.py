import threading
from queue import Queue
from time import sleep
from random import randint


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe():
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables
        
    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table.guest = guest
                    break
            else:
                print(f'{guest.name} в очереди')
                self.queue.put(guest)

    def discuss_guests(self):
        while self.queue.empty() == False or any([table.guest for table in self.tables]):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
