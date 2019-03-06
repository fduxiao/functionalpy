from .monad import Monad


class Maybe(Monad):
    def __init__(self, data, nothing=False):
        self.data = data
        self._nothing = nothing

    @staticmethod
    def nothing():
        return Maybe(None, nothing=True)

    @property
    def just(self):
        return not self._nothing

    @staticmethod
    def ret(value) -> "Maybe":
        return Maybe(value, nothing=False)

    def bind(self, f):
        if self._nothing:
            return self
        return f(self.data)

    def __repr__(self):
        if self.just:
            return f"Just {self.data}"
        return "Nothing"
