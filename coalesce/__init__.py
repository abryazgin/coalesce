__version__ = '0.1'


class UniqueValue(object):
    """
    Simple, unique object
    """
    __slots__ = ('truthful',)

    def __init__(self, truthful=None):
        self.truthful = truthful

    def __nonzero__(self):
        if self.truthful is None:
            raise TypeError('UniqueValue is not declared as truthful or falsely')
        return self.truthful


"""
Empty-object
"""
empty = UniqueValue(truthful=False)


def coalesce(iterable, ignore=empty, default=empty):
    """
    Return first not empty value from iterable object

    :param iterable - some iterable object
    :param ignore - ignoring value
    :param default - value which returning if all values are `exclude`-values
    :return first not empty value
    """
    return first(lambda x: x != ignore, iterable, default=default)


def first(function, iterable, default=None):
    """
    Return first value from iterable object for which the `function(value)` is truthful

    :param function - some filter-function which returns some logical value
    :param iterable - some iterable object
    :param default - default which returns, when not occurs value with truthful result for `function(value)`
    :return first value from iterable object for which the `function(value)` is truthful
    """
    for value in iterable:
        if function(value):
            return value
    return default
