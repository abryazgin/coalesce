from coalesce import coalesce, empty, first, UniqueValue


def test_unique_value():
    val = UniqueValue()
    assert val == val
    assert val is val
    assert UniqueValue() != UniqueValue()
    assert UniqueValue() is not UniqueValue()


def test_empty():
    assert empty == empty
    assert empty is empty
    assert not bool(empty)


def test_coalesce():
    assert coalesce([None, 1]) is None
    assert coalesce((empty, 'string', 1)) is 'string'
    assert coalesce((empty, None)) is None
    assert coalesce((empty, None)) is None
    assert coalesce((empty, empty)) is empty
    assert coalesce((empty, empty), default=1) is 1
    assert coalesce((1, 1), ignore=1) is empty
    assert coalesce((1, 1), ignore=1, default=-4) is -4
    assert coalesce((), default=8) is 8


def test_first():
    array = [0, 2, 7, None]
    assert first(lambda x: x > 3, array) is 7
    assert first(lambda x: x >= 0, array) is 0
    assert first(lambda x: x, array) is 2
    assert first(lambda x: x is None, array, default='default') is None
    assert first(lambda x: x is not None and x > 10, array, default='default') is 'default'
