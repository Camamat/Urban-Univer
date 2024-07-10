class Car():
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int):
            True
        else:
            raise IncorrectVinNumber("Некорректный тип vin номер")

        if 1000000 < vin_number < 9999999:
            True
        else:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')


    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            True
        else:
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) == 6:
            True
        else:
            raise IncorrectCarNumbers('Неверная длина номера')

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message



try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

