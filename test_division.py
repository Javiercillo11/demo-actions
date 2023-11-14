import unittest
from division import division

class TestDivision(unittest.TestCase):
    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(2, 2), 1)
        self.assertEqual(division(6, 2), 3)

if __name__ == '__main__':
    unittest.main()
        