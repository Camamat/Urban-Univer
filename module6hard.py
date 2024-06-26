import math

class Figure:

    sides_count = 0

    def __init__(self, color, *sides, filled = False):
        if len(sides) != self.sides_count:
            self.__sides = [1 * self.sides_count]
        else:
            self.__sides = []
            for i in sides:
                self.__sides.append(i)
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b) -> bool:

        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)

    def __is_valid_sides(self, sides):
        _list = []
        for i in sides:
            if i > 0:
                _list.append(i)
        if len(_list) > 0 and len(sides) == len(self.__sides):
            return True
        else:
            return False

    def set_sides(self, *number_of_sides):
        if self.__is_valid_sides(number_of_sides):
            self.__sides = number_of_sides

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):

    sides_count = 1

    def __radius(self):
        return self.__len__ * (2/pi)

    def get_square(self):
        return (self.__len__**2)/(4*pi)


class Triangle(Figure):
    sides_count = 3

    def __height(self):
        sp = self.__len__/2
        h = (2**(sp(sp-self.__sides[0])(sp-self.__sides[1])(sp-self.__sides[2])))/2*sp
        return h

    def get_square(self):
        sp = self.__len__/2
        s = sqrt((sp(sp - self.__sides[0])(sp-self.__sides[1])(sp-self.__sides[2])))
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color,  *sides, filled = True):
        super().__init__(color, *sides, filled)
        if len(sides) == 1:
            for i in sides:
                self.__sides = self.sides_count * [i]
        else:
            self.__sides = [1*self.sides_count]

    def get_sides(self):
        return [*self.__sides]

    def get_volume(self):
        return self.__sides[1]**3




circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
cube1.set_color(300, 70, 15)
print(circle1.get_color())
print(cube1.get_color())
cube1.set_sides(5, 3, 12, 4, 5)
circle1.set_sides(15)
print(cube1.get_sides())
print(circle1.get_sides())
print(len(circle1))
print(cube1.get_volume())
