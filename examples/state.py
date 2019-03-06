from functionalpy.monad import do, State


@do
def state(postfix) -> State:
    s = yield State.get()
    s += postfix
    yield State.put(s)
    s = yield State.get()
    return State.ret(len(s))


if __name__ == '__main__':
    print(state("postfix").run("start"))
