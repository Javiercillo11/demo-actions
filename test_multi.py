import unittest
from multi import multi

class TestMulti(unittest.TestCase):
    def test_multi(self):
        self.assertEqual(multi(3, 2), 6)
        self.assertEqual(multi(5, 5), 25)
        self.assertEqual(multi(2, 2), 4)

if __name__ == '__main__':
    unittest.main()
        