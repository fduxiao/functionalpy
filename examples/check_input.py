from functionalpy.monad import Maybe, do


def my_input(prompt="input a number: ") -> Maybe:
    v = input(prompt)
    for x in v:
        if x not in "0123456789":
            return Maybe.nothing()
    return Maybe.ret(int(v))


@do
def my_add():
    a1 = yield my_input('number1: ')
    a2 = yield my_input('number2: ')
    return Maybe(a1 + a2)


if __name__ == '__main__':
    print(my_add())

