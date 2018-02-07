# Python bindings for libversion

[![Build Status](https://travis-ci.org/repology/py-libversion.svg?branch=master)](https://travis-ci.org/repology/py-libversion)

## Purpose

Provides a fast implementation of advanced generic version string
comparison algorithm.

See [libversion](https://github.com/repology/libversion) repository
for more details on the algorithm.

## Features

* Provides API similar to C library, `version_compare(a, b)` function
* Provides more pythonic `Version` class with overloaded comparison operators

## Requirements

* Python 3.4+
* [libversion](https://github.com/repology/libversion) 2.5.0+

## Example

```python
from libversion import Version

assert(Version("1.0") == Version("001.0.0"))

assert(Version("0.999") < Version("1.0alpha1"))
assert(Version("1.0alpha1") < Version("1.0alpha2"))
assert(Version("1.0alpha2") < Version("1.0beta1"))
assert(Version("1.0beta1") < Version("1.0pre1"))
assert(Version("1.0pre1") < Version("1.0rc1"))
assert(Version("1.0rc1") < Version("1.0"))
assert(Version("1.0") < Version("1.0patch1"))
```

## License

MIT license, copyright (c) 2018 Dmitry Marakasov <amdmi3@amdmi3.ru>.
