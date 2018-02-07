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

from libversion import ANY_IS_PATCH_LEFT, ANY_IS_PATCH_RIGHT, P_IS_PATCH_LEFT, P_IS_PATCH_RIGHT, version_compare


class TestLibVersion(unittest.TestCase):
    def test_cversion_compare_no_flags(self):
        self.assertEqual(version_compare('001.001', '1.1'), 0)
        self.assertEqual(version_compare('1.0010', '1.01'), 1)
        self.assertEqual(version_compare('1.0', '1.0a'), -1)

    def test_cversion_compare_flag_p_is_patch(self):
        self.assertEqual(version_compare('1.0p1', '1.0p1', P_IS_PATCH_RIGHT), -1)
        self.assertEqual(version_compare('1.0p1', '1.0p1', P_IS_PATCH_LEFT), 1)

    def test_cversion_compare_flag_any_is_patch(self):
        self.assertEqual(version_compare('1.0a1', '1.0a1', ANY_IS_PATCH_RIGHT), -1)
        self.assertEqual(version_compare('1.0a1', '1.0a1', ANY_IS_PATCH_LEFT), 1)


if __name__ == '__main__':
    unittest.main()
