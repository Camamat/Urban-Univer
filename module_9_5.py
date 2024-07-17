class StepValueError(ValueError):
    pass

class Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = 0
        if self.step == 0:
            raise StepValueError('Шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start - self.step
        return self

    def __next__(self):
        self.pointer += self.step
        if self.step > 0:
            if self.pointer > self.stop:
                raise StepValueError()
        if self.step < 0:
            if self.pointer < self.stop:
                raise StepValueError()
        return self.pointer

        raise StopIteration()

