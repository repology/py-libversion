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

import unittest

from libversion import ANY_IS_PATCH, LOWER_BOUND, P_IS_PATCH, UPPER_BOUND, version_compare


class TestLibVersion(unittest.TestCase):
    def test_cversion_compare_no_flags(self) -> None:
        self.assertEqual(version_compare('001.001', '1.1'), 0)
        self.assertEqual(version_compare('1.0010', '1.01'), 1)
        self.assertEqual(version_compare('1.0', '1.0a'), -1)

    def test_cversion_compare_flag_p_is_patch(self) -> None:
        self.assertEqual(version_compare('1.0p1', '1.0p1', 0, P_IS_PATCH), -1)
        self.assertEqual(version_compare('1.0p1', '1.0p1', P_IS_PATCH, 0), 1)

    def test_cversion_compare_flag_any_is_patch(self) -> None:
        self.assertEqual(version_compare('1.0a1', '1.0a1', 0, ANY_IS_PATCH), -1)
        self.assertEqual(version_compare('1.0a1', '1.0a1', ANY_IS_PATCH, 0), 1)

    @unittest.skipIf(LOWER_BOUND == 0 or UPPER_BOUND == 0, 'LOWER_BOUND/UPPER_BOUND flags are not supported by underlying libversion, please update it to 3.0.0')
    def test_cversion_compare_bound_flags(self) -> None:
        self.assertEqual(version_compare('1.0a1', '1.0', 0, 0), -1)
        self.assertEqual(version_compare('1.0a1', '1.0', 0, LOWER_BOUND), 1)

        self.assertEqual(version_compare('1.0.1', '1.0', 0, 0), 1)
        self.assertEqual(version_compare('1.0.1', '1.0', 0, UPPER_BOUND), -1)


if __name__ == '__main__':
    unittest.main()
