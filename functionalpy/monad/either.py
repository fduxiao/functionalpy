from .monad import Monad


class Either(Monad):
    Left = 0
    Right = 1

    def __init__(self, value, status):
        self.value = value
        self.status = status

    @staticmethod
    def left(value):
        return Either(value, Either.Left)

    @staticmethod
    def right(value):
        return Either(value, Either.Right)

    ret = right

    def bind(self, f):
        if self.status is Either.Left:
            return self
        else:
            return f(self.value)

    def __repr__(self):
        if self.status is Either.Left:
            return f"Left {self.value}"
        return f"Right {self.value}"
