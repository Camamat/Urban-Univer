class Buiding:
    total = 0
    def __init__(self):
        Buiding.total +=1

for i in range(1, 41):
    Buiding()

print(Buiding.total)