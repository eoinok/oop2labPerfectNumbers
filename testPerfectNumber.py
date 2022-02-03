import unittest
from perfectNumber import perfectNumber


class TestPefectNumber(unittest.TestCase):

      def test_perfect_number(self):
        testNum = 8128
        self.assertTrue(perfectNumber(testNum))

if __name__ == '__main__':
    unittest.main()
