import unittest
import json
from main import *

class Test_convert_file_to_stemmed_word_count_dict(unittest.TestCase):

    def test_simple_files(self):
        test_cases = [
            {
                "file_path": "test_data/empty.txt",
                "expected_dict": {}
            },
            {
                "file_path": "test_data/multiple-lines.txt",
                "expected_dict": {"some": 2, "word":2, "in": 2, "a": 1, "column":2, "with": 1, "repeat": 1, "that":1}
            },
            {
                "file_path": "test_data/single-line.txt",
                "expected_dict": {"some": 2, "word":2, "in": 2, "a": 1, "row":2, "with": 1, "repeat": 1, "that":1}
            }
        ]

        for test_case in test_cases:
            actual_dict = convert_file_to_stemmed_word_count_dict(test_case["file_path"])
            for k,v in test_case["expected_dict"].items():
                self.assertEqual(v, actual_dict[k], f'expected {v} of {k}, found {actual_dict[k]}.')
            self.assertEqual(len(actual_dict.keys()), len(test_case["expected_dict"].keys()))

if __name__ == "__main__":
    unittest.main()