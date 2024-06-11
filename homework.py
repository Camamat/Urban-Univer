class house:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

A = house(0)
A.setNewNumberOfFloors(4)

