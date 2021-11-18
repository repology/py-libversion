# Python bindings for libversion

<a href="https://repology.org/metapackage/python:libversion/versions">
	<img src="https://repology.org/badge/vertical-allrepos/python:libversion.svg" alt="py-libversion packaging status" align="right">
</a>

[![CI](https://github.com/repology/py-libversion/actions/workflows/ci.yml/badge.svg)](https://github.com/repology/py-libversion/actions/workflows/ci.yml)
[![PyPI downloads](https://img.shields.io/pypi/dm/libversion.svg)](https://pypi.org/project/libversion/)
[![PyPI version](https://img.shields.io/pypi/v/libversion.svg)](https://pypi.org/project/libversion/)
[![PyPI pythons](https://img.shields.io/pypi/pyversions/libversion.svg)](https://pypi.org/project/libversion/)
[![Github commits (since latest release)](https://img.shields.io/github/commits-since/repology/py-libversion/latest.svg)](https://github.com/repology/py-libversion)

## Purpose

Python bindings for libversion, which provides **fast**, **powerful**
and **correct** generic version string comparison algorithm.

See [libversion](https://github.com/repology/libversion) repository for
more details on the algorithm.

## Performance

**libversion** is 10x to 100x faster than other version comparison
facilities widely used in Python world.

| Facility                            | comps/sec |
|-------------------------------------|----------:|
| **libversion.version_compare2**     |  3492.81K |
| **libversion.version_compare**      |  3219.02K |
| **libversion.Version**              |   374.08K |
| tuple(map(int, (v.split('.'))))     |   206.02K |
| cmp_version.cmp_version             |   189.15K |
| cmp_version.VersionString           |   156.42K |
| distutils.version.StrictVersion     |    75.00K |
| version.Version                     |    71.39K |
| distutils.version.LooseVersion      |    51.38K |
| pkg_resources.parse_version         |    22.26K |

## Correctness

**libversion** handles certain complex version cases better than other
version comparison facilities. Here are some example cases where others
fail:

| Test case               | libversion | tuple         | StrictVersion | LooseVersion  | parse_version | cmp_version   |
|-------------------------|------------|---------------|---------------|---------------|---------------|---------------|
| 1.0 == 1.0.0            | ok         | incorrect (<) | ok            | incorrect (<) | ok            | ok            |
| 1.2_3 == 1.2-3          | ok         | fail          | fail          | incorrect (>) | incorrect (<) | ok            |
| 1.2.3 == 1.2-3          | ok         | fail          | fail          | fail          | incorrect (>) | incorrect (<) |
| 1.0alpha1 == 1.0.alpha1 | ok         | fail          | fail          | ok            | ok            | incorrect (>) |
| 1.0rc1 < 1.0            | ok         | fail          | fail          | incorrect (>) | ok            | incorrect (>) |
| 1.0 < 1.0patch1         | ok         | fail          | fail          | ok            | incorrect (>) | ok            |
| 1.0.2a < 1.0.2g         | ok         | fail          | fail          | ok            | incorrect (>) | ok            |

Note 1: **fail** means that attempt to compare versions has thrown
an exception, usually bacause a library cannot parse specific version
string.

Note 2: **version** module was not able to complete any tests as it's
a strict semantic version implementation which require 3 version
components. Also, it does not support Python 3 without modification.

## Python wrapper features

-  Provides API similar to C library, `version_compare(a, b)` function
-  Provides more pythonic (but slower) `Version` class with overloaded
   comparison operators

## Requirements

-  Python 3.6+
-  pkg-config
-  [libversion](https://github.com/repology/libversion) 2.7.0+

## Example code

```python
from libversion import Version, version_compare

assert(version_compare("0.9", "1.1") < 0)
assert(version_compare("1.0", "1.0.0") == 0)
assert(version_compare("1.1", "0.9") > 0)

assert(Version("0.9") < Version("1.1"))
assert(Version("1.0") ==  Version("1.0.0"))
assert(Version("1.1") > Version("0.9"))

assert(Version("0.999") < Version("1.0alpha1"))
assert(Version("1.0alpha1") < Version("1.0alpha2"))
assert(Version("1.0alpha2") < Version("1.0beta1"))
assert(Version("1.0beta1") < Version("1.0pre1"))
assert(Version("1.0pre1") < Version("1.0rc1"))
assert(Version("1.0rc1") < Version("1.0"))
assert(Version("1.0") < Version("1.0patch1"))
```

## License

MIT license, copyright (c) 2017-2018 Dmitry Marakasov amdmi3@amdmi3.ru.
