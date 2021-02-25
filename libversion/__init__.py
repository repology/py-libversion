# Copyright (c) 2019-2020 Dmitry Marakasov <amdmi3@amdmi3.ru>
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

from typing import Any, Union

from libversion._libversion import ANY_IS_PATCH as ANY_IS_PATCH
from libversion._libversion import LOWER_BOUND as LOWER_BOUND
from libversion._libversion import P_IS_PATCH as P_IS_PATCH
from libversion._libversion import UPPER_BOUND as UPPER_BOUND
from libversion._libversion import version_compare as version_compare
from libversion._libversion import version_compare2 as version_compare2
from libversion._libversion import version_compare4 as version_compare4


__version__ = '1.2.2'

__all__ = [
    'version_compare2',
    'version_compare4',
    'version_compare',

    'ANY_IS_PATCH',
    'P_IS_PATCH',
    'LOWER_BOUND',
    'UPPER_BOUND',

    'Version'
]


class Version:
    __slots__ = ['value', 'flags']

    P_IS_PATCH = P_IS_PATCH
    ANY_IS_PATCH = ANY_IS_PATCH
    LOWER_BOUND = LOWER_BOUND
    UPPER_BOUND = UPPER_BOUND

    def __init__(self, value: str, flags: int = 0) -> None:
        self.value = value
        self.flags = flags

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other: Any) -> Union[bool, 'NotImplemented']:
        if isinstance(other, Version):
            return version_compare(self.value, other.value, self.flags, other.flags) == 0
        return NotImplemented

    def __ne__(self, other: Any) -> Union[bool, 'NotImplemented']:
        if isinstance(other, Version):
            return version_compare(self.value, other.value, self.flags, other.flags) != 0
        return NotImplemented

    def __lt__(self, other: Any) -> Union[bool, 'NotImplemented']:
        if isinstance(other, Version):
            return version_compare(self.value, other.value, self.flags, other.flags) < 0
        return NotImplemented

    def __le__(self, other: Any) -> Union[bool, 'NotImplemented']:
        if isinstance(other, Version):
            return version_compare(self.value, other.value, self.flags, other.flags) <= 0
        return NotImplemented

    def __gt__(self, other: Any) -> Union[bool, 'NotImplemented']:
        if isinstance(other, Version):
            return version_compare(self.value, other.value, self.flags, other.flags) > 0
        return NotImplemented

    def __ge__(self, other: Any) -> Union[bool, 'NotImplemented']:
        if isinstance(other, Version):
            return version_compare(self.value, other.value, self.flags, other.flags) >= 0
        return NotImplemented
