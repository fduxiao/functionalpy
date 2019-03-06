from .monad import Monad


class State(Monad):
    def __init__(self, run_state):
        self.run_state = run_state

    def run(self, s):
        return self.run_state(s)

    @staticmethod
    def ret(value):
        return State(lambda s: (value, s))

    def bind(self, f):
        def run_state(s):
            a, new_s = self.run_state(s)
            return f(a).run(new_s)
        return State(run_state)

    @staticmethod
    def get():
        return State(lambda s: (s, s))

    @staticmethod
    def put(s):
        return State(lambda _: (None, s))
