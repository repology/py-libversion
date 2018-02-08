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

from competitors import competitors

from tabulate import tabulate


def get_cmp_sign(a, b):
    """Convert comparison result to single character representation."""
    if a < b:
        return '<'
    elif a > b:
        return '>'
    return '='


def evaluate_single_case(test_case, competitors):
    left, expected, right = test_case.split(' ')

    for _, wrapper in competitors:
        try:
            result = get_cmp_sign(wrapper(left), wrapper(right))
            yield 'ok' if result == expected else 'incorrect (' + result + ')'
        except:
            yield 'fail'


def evaluate_all_cases(test_cases, competitors):
    return [
        [test_case] + list(evaluate_single_case(test_case, competitors))
        for test_case in test_cases
    ]


test_cases = [
    '1.0 = 1.0',
    '1.0 = 1.00',
    '1.0 = 01.0',
    '1.0 = 1.0.0',
    '1.0 = 1..0',
    '1.2_3 = 1.2-3',
    '1.2.3 = 1.2-3',
    '1.0alpha1 = 1.0.alpha1',
    '0.9 < 1.0',
    '0.9 < 1.0alpha1',
    '1.0alpha1 < 1.0alpha2',
    '1.0alpha2 < 1.0beta1',
    '1.0beta1 < 1.0pre1',
    '1.0beta1 < 1.0rc1',
    '1.0pre1 < 1.0',
    '1.0rc1 < 1.0',
    '1.0 < 1.0patch1',
    '1.0 < 1.0pl1',
    '1.0 < 1.0post1',
    '1.0.2 < 1.0.2a',
    '1.0.2a < 1.0.2g',
]


print(
    tabulate(
        evaluate_all_cases(test_cases, competitors),
        headers=['Test case'] + [competitor[0] for competitor in competitors]
    )
)
