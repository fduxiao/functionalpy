from math import sqrt

from functionalpy.monad import do, Either


def safe_div(a, b) -> Either:
    if b == 0:
        return Either.left("ZeroDivision")
    return Either.ret(a/b)


def safe_sqrt(a) -> Either:
    if a < 0:
        return Either.left("Sqrt of a negative number")
    return Either.ret(sqrt(a))


@do
def cal(a, b):
    root = yield safe_sqrt(a)
    quotient = yield safe_div(root, b)
    return Either.ret(quotient)


if __name__ == '__main__':
    print(cal(1, 2))
    print(cal(1, 0))
    print(cal(-1, 1))
    print(cal(-1, 0))
