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

__all__ = [
    'competitors',
]


competitors = [
    (
        'libversion.version_compare', 'libversion',
        'import libversion',
        'libversion.version_compare({}, {})', '0',
        2_600_000
    ),
    (
        'libversion.Version', None,
        'import libversion',
        'libversion.Version({})', 'libversion.Version({})',
        230_000
    ),
    (
        'tuple(map(int, (v.split("."))))', 'tuple',
        '',
        'tuple(map(int,({}.split("."))))', 'tuple(map(int,({}.split("."))))',
        200_000
    ),
    (
        'cmp_version.cmp_version', 'cmp_version',
        'import cmp_version',
        'cmp_version.cmp_version({}, {})', '0',
        200_000
    ),
    (
        'cmp_version.VersionString', None,
        'import cmp_version',
        'cmp_version.VersionString({})', 'cmp_version.VersionString({})',
        150_000
    ),
    (
        'distutils.version.StrictVersion', 'StrictVersion',
        'import distutils.version',
        'distutils.version.StrictVersion({})', 'distutils.version.StrictVersion({})',
        75_000
    ),
    (
        'version.Version', 'version',
        'import version',
        'version.Version({})', 'version.Version({})',
        60_000
    ),
    (
        'distutils.version.LooseVersion', 'LooseVersion',
        'import distutils.version',
        'distutils.version.LooseVersion({})', 'distutils.version.LooseVersion({})',
        50_000
    ),
    (
        'pkg_resources.parse_version', 'parse_version',
        'import pkg_resources',
        'pkg_resources.parse_version({})', 'pkg_resources.parse_version({})',
        20_000
    ),
]
