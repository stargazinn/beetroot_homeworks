import unittest
from functools import wraps
from ht_13 import *

class TestHT13(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_create_slogan(self):
        self.assertEqual(create_slogan('S@SH05'),
                         'S@SH05 drinks pepsi in his brand new BMW!')

    def test_arg_rules(self):
        self.assertIsInstance(create_slogan('S@SH05'), str)



# unittest.main()
if __name__ == '__main__':
    unittest.main()