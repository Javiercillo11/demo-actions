import unittest
from resta import restar

class TestSumar(unittest.TestCase):
    def test_restar(self):
        self.assertEqual(restar(4, 2), 2)
        self.assertEqual(restar(1, 1), 0)
        self.assertEqual(restar(2, 1), 1)

if __name__ == '__main__':
    unittest.main()