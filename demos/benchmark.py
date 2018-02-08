#!/usr/bin/env python3
# Copyright (c) 2018 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from timeit import timeit


def benchmark(name, stmt, setup, number=100000):
    time = timeit(stmt=stmt, setup=setup, number=number)

    print('{:>20}: {:.2f} K/sec'.format(name, number / time / 1000.0))


# number of iterations is tweaked so all tests take approx the same time
benchmark('version_compare', 'version_compare("1.2.3", "2.3.4")', 'from competitors import version_compare', 3400000)
benchmark('Version class', 'Version("1.2.3") < Version("2.3.4")', 'from competitors import Version', 220000)
benchmark('versiontuple', 'versiontuple("1.2.3") < versiontuple("2.3.4")', 'from competitors import versiontuple', 190000)
benchmark('StrictVersion', 'StrictVersion("1.2.3") < StrictVersion("2.3.4")', 'from competitors import StrictVersion', 70000)
benchmark('LooseVersion', 'LooseVersion("1.2.3") < LooseVersion("2.3.4")', 'from competitors import LooseVersion', 50000)
benchmark('parse_version', 'parse_version("1.2.3") < parse_version("2.3.4")', 'from competitors import parse_version', 20000)
