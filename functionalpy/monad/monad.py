#!/usr/bin/env python3
from functools import wraps


class Monad:
    @staticmethod
    def ret(value):
        pass

    def bind(self, f):
        return


# this will always make a new generator, which is unnecessary
# def partial_apply(generator, x):
#     while True:
#         try:
#             x = yield generator.send(x)
#         except StopIteration as err:
#             return err.value


class _Generator:
    class _Null:
        pass

    def __init__(self, generator):
        self._generator = generator
        self._x = _Generator._Null

    @staticmethod
    def new(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            return _Generator(f(*args, **kwargs))
        return wrapper

    def __next__(self):
        if self._x is not _Generator._Null:
            x = self._x
            self._x = _Generator._Null
            return self._generator.send(x)
        return next(self._generator)

    def __iter__(self):
        return self

    def send(self, x):
        return self._generator.send(x)

    def partial_apply(self, x):
        self._x = x
        return self

    def __repr__(self):
        return f"Generator {self._generator.__repr__()}"


# def reduce(generator):
#     try:
#         m_a = next(generator)
#     except StopIteration as err:
#         return err.value
#
#     return m_a.bind(lambda a: reduce(partial_apply(generator, a)))


def reduce(generator: _Generator):
    try:
        m_a = generator.__next__()
    except StopIteration as err:
        return err.value

    return m_a.bind(lambda a: reduce(generator.partial_apply(a)))


def do(generator_func):
    @wraps(generator_func)
    def wrapper(*args, **kwargs):
        generator = _Generator(generator_func(*args, **kwargs))
        return reduce(generator)
    return wrapper
