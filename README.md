# Awesome decorators

[![Build Status](https://travis-ci.org/romaryd/python-awesome-decorators.svg?branch=master)](https://travis-ci.org/romaryd/python-awesome-decorators)
[![Coverage Status](https://coveralls.io/repos/github/romaryd/python-awesome-decorators/badge.svg?branch=master)](https://coveralls.io/github/romaryd/python-awesome-decorators?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/b03f759c2a1d62011a6d/maintainability)](https://codeclimate.com/github/romaryd/python-awesome-decorators/maintainability)
[![Code Health](https://landscape.io/github/romaryd/python-awesome-decorators/master/landscape.svg?style=flat)](https://landscape.io/github/romaryd/python-awesome-decorators/master)

List of awesome decorators that could be useful in Python projects.

## Installation

```
pip install python-awesome-decorators
```

## Decorators

### memoized

Return a property attribute for new-style classes that only calls its
getter on the first access. The result is stored and on subsequent
accesses is returned, preventing the need to call the getter any more.


``` python
from awesomedecorators import memoized

class Example:
  @memoized
  def my_property(self):
    # Do something that takes time and we want it to happen once
```

### timeit

Return the time taken by a function to complete.

``` python
from awesomedecorators import timeit

@timeit
def myfunc(a):
  return a + 5

result, elapsed = myfunc(10)
print('this function took {} ms'.format(elapsed))
```

### timeout

Raise a ``TimeoutError`` exception if a function does not complete before a
certain duration specified in seconds.

``` python
import time
from awesomedecorators import timeout

@timeout(2)
def myfunc(duration):
    time.sleep(duration)

try:
  myfunc(3)
except TimeoutError:
  print('Time out !')
  pass
```
