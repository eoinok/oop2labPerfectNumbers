import unittest
from divisors import divisors

class TestDivisors(unittest.TestCase):

    def test_divisors(self):
        num = 28
        divisorList = [1,2,4,7,14]
        result = divisors(num)
        self.assertEqual(result, divisorList)


if __name__ == '__main__':
    unittest.main()
