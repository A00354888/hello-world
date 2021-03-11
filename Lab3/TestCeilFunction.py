'''
    Right - Easy test just to validate that the function does what it has to do
    B - I just found a test case which could be useful. Validate that the return value from ceil() function is an int for Python3 or a float for Python2
    I - I did not find any test case for Inverse relationships test
    C - I did not find any test case for Cross-check test
    E - I used very high and low values to validate that the function works as expected. There is a limit at 99999999999999999999999.1, the function returned the value 99999999999999991611392
        Also for negative values there is a limit.
    P - I did not find any test case for Performance test
'''

import unittest
import math
import sys

class TestMathCeilFunction(unittest.TestCase):

    def test_positive1(self):
        self.assertEqual(math.ceil(1.1), 2)

    def test_positive2(self):
        self.assertEqual(math.ceil(-2.3), -2)

    def test_positive3(self):
        self.assertEqual(math.ceil(10000000000), 10000000000)

    @unittest.skipIf(sys.version_info < (3,0), "Python2 returns a float value")
    def test_is_integer(self):        
        self.assertTrue(type(math.ceil(1.1)) == int)

    @unittest.skipIf(sys.version_info >= (3,0), "Python3 returns an integer value")
    def test_is_float(self):        
        self.assertTrue(type(math.ceil(1.1)) == float)
    
    def test_very_high_value(self):
        self.assertEqual(math.ceil(9999999999999999999999.1), 10000000000000000000000)

    def test_very_low_value(self):
        self.assertEqual(math.ceil(-9999999999999999999999.1), 9999999999999999999998)


if __name__ == '__main__':
    unittest.main()