import abc


class Base(object):
    """
    Example docstring comment.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, name):
        self._name = name  # Example inline comment

    @property
    def name(self):
        return "Hello, {name}".format(name=self.name)

    @abc.abstractmethod
    def foo(self, itetable, func):
        pass


class Derived(Base):
    def foo(self, iterable, func):
        return [func(x) for x in iterable]


if __name__ == '__main__':
    for x in Derived(1337).foo(range(10), func=lambda x: x**2):
        print(x)

    raise SystemExit(0)
