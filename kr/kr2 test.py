import unittest
from kr2 import process_scores
class TestProcessScores(unittest.TestCase):

    def test_above_average_students(self):
        scores = [
            ('Alice', 85),
            ('Bob', 75),
            ('Charlie', 39),
            ('David', 62),
            ('Eve', 91)
        ]
        expected_output = {
            'Eve': 91,
            'Alice': 85,
            'Bob': 75
        }
        self.assertEqual(process_scores(scores), expected_output)

    def test_all_below_average(self):
        scores = [
            ('Alice', 20),
            ('Bob', 30),
            ('Charlie', 10),
            ('David', 15)
        ]
        expected_output = {
            'Bob': 30,
            'Alice': 20
        }
        self.assertEqual(process_scores(scores), expected_output)

    def test_all_above_average(self):
        scores = [
            ('Alice', 90),
            ('Bob', 80),
            ('Charlie', 85),
            ('David', 95)
        ]
        expected_output = {
            'David': 95,
            'Alice': 90,
        }
        self.assertEqual(process_scores(scores), expected_output)

    def test_single_student(self):
        scores = [
            ('Alice', 85)
        ]
        expected_output = {}
        self.assertEqual(process_scores(scores), expected_output)

    def test_empty_list(self):
        scores = []
        expected_output = {}
        self.assertEqual(process_scores(scores), expected_output)

if __name__ == '__main__':
    unittest.main()
