#!/usr/bin/env python3
from functools import wraps


class Monad:
    @staticmethod
    def ret(value):
        pass

    def bind(self, f):
        return


def partial_apply(generator, x):
    while True:
        try:
            x = yield generator.send(x)
        except StopIteration as err:
            return err.value


def reduce(generator):
    try:
        m_a = next(generator)
    except StopIteration as err:
        return err.value

    return m_a.bind(lambda a: reduce(partial_apply(generator, a)))


def do(generator_func):
    @wraps(generator_func)
    def wrapper(*args, **kwargs):
        return reduce(generator_func(*args, **kwargs))
    return wrapper
