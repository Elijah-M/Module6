import unittest
from more_functions.validate_input_in_functions import score_input

class ValidateTest(unittest.TestCase):
    """
    def test_score_input_test_name(self):
        self.assertEqual(score_input(test_name="Elijah"), "Elijah")

    def test_score_input_test_score_valid(self):
        self.assertEqual(score_input(test_name="Elijah", test_score=9), 9)

    def test_score_input_test_score_below_range(self):
        self.assertEqual(score_input(test_name="Elijah", test_score=-2), -2)

    def test_score_input_test_score_above_range(self):
        self.assertEqual(score_input(test_name="Elijah", test_score=333), 333)
    """
    def test_test_score_non_numeric(self):
        self.assertEqual(score_input(test_name="Elijah", test_score='E'), 'E')
    """
    def test_score_input_invalid_message(self):
        self.assertEqual()
    """

if __name__ == '__main__':
    unittest.main()
