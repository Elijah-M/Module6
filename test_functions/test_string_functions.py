import unittest
from more_functions.string_functions import multiply_string

class test_string_functions(unittest.TestCase):
    def test_multiple_string(self):
        self.multiply_string("Hello", 5)


if __name__ == '__main__':
    unittest.main()