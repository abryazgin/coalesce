# coalesce
Simple Python library with coalesce function and "magic" empty value and 
others features

## Installation

```
pip install coalesce
```

## Features
### UniqueValue

This is a factory of some abstract unique values

Example:

```python
from coalesce import UniqueValue

Yes = UniqueValue(truthful=True)
MayBe = UniqueValue()
IDontKnow = UniqueValue()
Unlikely = UniqueValue()
No = UniqueValue(truthful=False)


def answer_lottery():
    import random
    return random.choice((Yes, MayBe, IDontKnow, Unlikely, No))


print("- Are you hungry?")
hungry_answer = answer_lottery()
try:
    if hungry_answer:
        print("- YES, i would eat an elephant!")
    else:
        print("- I'm fed up...")
except TypeError:
    print("- Well, I want only coffee")


print("- Will you marry me?")
marry_answer = answer_lottery()
if marry_answer == Yes:
    print("- Well, finally, YES!")
elif marry_answer == MayBe:
    print("- Well, only if you really are rich...")
elif marry_answer == IDontKnow:
    print("- I need to think...")
elif marry_answer == Unlikely:
    print("- When the cancer on the mountain whistles.")
elif marry_answer == No:
    print("- Who are you, boy?")
```

### empty
The `empty` is conrete falsely UniqueValue.

Using in situations, when we want differ None and real "empty" value.
For example set a dynamically calculated default value:

```python
from coalesce import empty
from random import randint


def f(value=empty):
    if value == empty:
        value = randint(1,10)
    print('value={}'.format(value))

f()  # value=<random(1,10)>
f(None)  # value=None
```

### coalesce
Function returns first not ignoring value from iterable object. 
By default ignoring `empty` value

Example:
```python
from coalesce import coalesce, empty
from random import randint


def f(value=empty):
    value = coalesce([value, randint(1,10)])
    print('value={}'.format(value))

f()  # value=<random(1,10)>
f(None)  # value=None

print coalesce([None, 1, 2], ignore=None, default=-7)  # 1
print coalesce([None, None], ignore=None, default=-7)  # -7
```

### first
Function returns first value from iterable 
for which the `function(value)` is truthful from iterable object. 
Else it returns default value

Example:
```python
from coalesce import first

print first(lambda x: x > 1, [None, 1, 2], default=-7)  # 2
print first(lambda x: x > 2, [None, 1, 2], default=-7)  # -7
```
