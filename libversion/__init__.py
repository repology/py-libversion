# Copyright (c) 2017-2018 Dmitry Marakasov <amdmi3@amdmi3.ru>
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

from libversion._libversion import ANY_IS_PATCH, ANY_IS_PATCH_LEFT, ANY_IS_PATCH_RIGHT, P_IS_PATCH, P_IS_PATCH_LEFT, P_IS_PATCH_RIGHT, version_compare


__version__ = '0.1.0'

__all__ = [
    'version_compare',

    'ANY_IS_PATCH',
    'ANY_IS_PATCH_LEFT',
    'ANY_IS_PATCH_RIGHT',
    'P_IS_PATCH',
    'P_IS_PATCH_LEFT',
    'P_IS_PATCH_RIGHT',

    'Version'
]


class Version:
    P_IS_PATCH = 0x1
    ANY_IS_PATCH = 0x2

    def __init__(self, value, flags=0):
        self.value = value
        self.flags = flags

    def _leftflags(self):
        flags = 0
        if self.flags & Version.P_IS_PATCH:
            flags |= P_IS_PATCH_LEFT
        if self.flags & Version.ANY_IS_PATCH:
            flags |= ANY_IS_PATCH_LEFT
        return flags

    def _rightflags(self):
        flags = 0
        if self.flags & Version.P_IS_PATCH:
            flags |= P_IS_PATCH_RIGHT
        if self.flags & Version.ANY_IS_PATCH:
            flags |= ANY_IS_PATCH_RIGHT
        return flags

    def _compare(self, other):
        return version_compare(
            self.value,
            other.value,
            self._leftflags() | other._rightflags()
        )

    def __str__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, Version):
            return self._compare(other) == 0
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Version):
            return self._compare(other) != 0
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return self._compare(other) < 0
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Version):
            return self._compare(other) <= 0
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Version):
            return self._compare(other) > 0
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Version):
            return self._compare(other) >= 0
        return NotImplemented
