# functionalpy
A tool set for functional programming in python

## Install
```shell
$ pip install .
```

## Monad
Monad in haskell is just a syntax sugar which chain the 
code flow without an embedding hell. Here I use python keyword
`yield` to avoid it.

A monad is defined just like what it should be:
```python
# Nothing special here
class Maybe:
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
    def ret(value):
        return Maybe(value, nothing=False)

    def bind(self, f):
        if self._nothing:
            return self
        return f(self.data)

    def __repr__(self):
        if self.just:
            return f"Just {self.data}"
        return "Nothing"

```

As in following code, one can use `yield` to suspend the execution
and give the monad. 

```python
def cal():
    a = yield Maybe(1)
    b = yield Maybe(2)
    return a + b
```

As is expected, one may use `next` to get the monad and then use 
the `bind` method to decide how to provoke the following execution via `send` of the generator.
```python
c = cal()
m_a = next(c)  # m_a is Maybe(1)
```
However we cannot send it directly. The rest of generator 
should be a function, which takes the bound value of m_a 
as `a` in `cal` and returns a new generator (with `a` fed),
so we need to apply it partially. 
```python
def partial_apply(generator, x):
    while True:
        try:
            x = yield generator.send(x)
        except StopIteration as err:
            return err.value
           
# and it is called as: 
def reduce(generator):
    try:
        m_a = next(generator)
    except StopIteration as err:
        return err.value
        
    return m_a.bind(lambda a: reduce(partial_apply(generator, a)))
```
I further write a decorator to perform the calculation automatically
like this:
```python
from functools import wraps


def do(generator_func):
    @wraps(generator_func)
    def wrapper(*args, **kwargs):
        return reduce(generator_func(*args, **kwargs))
    return wrapper
```

---

I turn them into a package with many implementations provided. 
Here's an example of how to use it. 
```python
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
```