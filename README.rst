Python bindings for libversion
==============================

|Build Status| |PyPI|

Purpose
-------

Provides **fast** and **correct** generic version string comparison
algorithm.

See `libversion`_ repository for more details on the algorithm.

Performace
----------

``libversion`` is 10x to 100x faster than other version comparison
facilities widely used in Python world.

+-------------------------------------+-----------+
| Facility                            | comps/sec |
+=====================================+===========+
| ``libversion.version_compare``      |  3219.02K |
+-------------------------------------+-----------+
| ``libversion.Version``              |   227.56K |
+-------------------------------------+-----------+
| ``tuple(map(int, (v.split('.'))))`` |   206.02K |
+-------------------------------------+-----------+
| ``distutils.version.StrictVersion`` |    75.00K |
+-------------------------------------+-----------+
| ``distutils.version.LooseVersion``  |    51.38K |
+-------------------------------------+-----------+
| ``pkg_resources.parse_version``     |    22.26K |
+-------------------------------------+-----------+

Correctness
-----------

``libversion`` handles certain complex version cases better than other
version comparison facilities. Here are some example cases where others
fail:

+-----------------+------------+---------------+---------------+---------------+---------------+
| Test case       | libversion | tuple         | StrictVersion | LooseVersion  | parse_version |
+=================+============+===============+===============+===============+===============+
| 1.0 = 1.0.0     | ok         | incorrect (<) | ok            | incorrect (<) | ok            |
+-----------------+------------+---------------+---------------+---------------+---------------+
| 1.2_3 = 1.2-3   | ok         | fail          | fail          | incorrect (>) | incorrect (<) |
+-----------------+------------+---------------+---------------+---------------+---------------+
| 1.2.3 = 1.2-3   | ok         | fail          | fail          | fail          | incorrect (>) |
+-----------------+------------+---------------+---------------+---------------+---------------+
| 1.0rc1 < 1.0    | ok         | fail          | fail          | incorrect (>) | ok            |
+-----------------+------------+---------------+---------------+---------------+---------------+
| 1.0 < 1.0patch1 | ok         | fail          | fail          | ok            | incorrect (>) |
+-----------------+------------+---------------+---------------+---------------+---------------+
| 1.0.2a < 1.0.2g | ok         | fail          | fail          | ok            | incorrect (>) |
+-----------------+------------+---------------+---------------+---------------+---------------+

Python wrapper features
-----------------------

-  Provides API similar to C library, ``version_compare(a, b)`` function
-  Provides more pythonic (but slower) ``Version`` class with overloaded
   comparison operators

Requirements
------------

-  Python 3.4+
-  pkg-config
-  `libversion`_ 2.5.0+

Example code
------------

.. code:: python

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

License
-------

MIT license, copyright (c) 2017-2018 Dmitry Marakasov amdmi3@amdmi3.ru.

.. _libversion: https://github.com/repology/libversion

.. |Build Status| image:: https://travis-ci.org/repology/py-libversion.svg?branch=master
   :target: https://travis-ci.org/repology/py-libversion
.. |PyPI| image:: https://img.shields.io/pypi/v/libversion.svg
   :target: https://pypi.python.org/pypi/libversion
