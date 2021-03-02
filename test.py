import unittest
import json
from main import *

# note: no effort was put in to attaching names to test cases
# this would be a higher priority if this was running a pipeline and it was a 
# regular task for humans or machines to parse errors
class Test_convert_file_to_stemmed_word_count_dict(unittest.TestCase):

    def test_simple_files(self):
        test_cases = [
            # white spaces, this could use more types, but spaces and line break seemed like a good place to start
            {
                "file_path": "test_data/whitespace.txt",
                "expected_dict": {"space": 1, "newlin": 1}
            },
            # makes sure non-alphabetical characters are removed. this is all of the base characters on my keyboard
            {
                "file_path": "test_data/non-alphabeticals.txt",
                "expected_dict": {"alphabet": 1}
            },
            # no input text means no output
            {
                "file_path": "test_data/empty.txt",
                "expected_dict": {}
            },
            # make sure each line gets read
            {
                "file_path": "test_data/multiple-lines.txt",
                "expected_dict": {"some": 2, "word":2, "in": 2, "a": 1, "column":2, "with": 1, "repeat": 1, "that":1}
            },
            # make sure each white-space separated word gets read
            {
                "file_path": "test_data/single-line.txt",
                "expected_dict": {"some": 3, "word":2, "in": 2, "a": 1, "row":2, "with": 1, "repeat": 1, "that":1}
            },
            # make sure the program gracefully handles an invalid file
            {
                "file_path": "notAFilePath(O*WPKIJNSEDGD",
                "expected_dict": {}
            },
            # make sure the program gracefully handles a directory
            {
                "file_path": "test_data/",
                "expected_dict": {}
            },
        ]

        for test_case in test_cases:
            actual_dict = convert_file_to_stemmed_word_count_dict(test_case["file_path"])
            # the error reporting here isn't ideal. this test data isn't too large to parse, but if test data becomes
            # larger, then a better visualization tool like deepdiff might be necessary
            self.assertEqual(actual_dict, test_case["expected_dict"], 
                             f'found dict \n{actual_dict} \nnot equal to expected \n{test_case["expected_dict"]}')

    def test_stop_words(self):
        # the case of no stop_words being passed in is covered by the test_simple_files cases
        test_cases = [
            # stop words equivalent to the given text should allow no words to return
            {
                "text_file_path": "test_data/multiple-lines.txt",
                "stop_words": {"some": 2, "word":2, "in": 2, "a": 1, "column":2, "with": 1, "repeat": 1, "that":1},
                "expected_dict": {}
            },
            # stop words should only block words from being counted when they ARE a stop word
            {
                "text_file_path": "test_data/multiple-lines.txt",
                "stop_words": {"some": 2, "word":2, "in": 2, "a": 1, "row":2, "with": 1, "repeat": 1, "that":1},
                "expected_dict": {"column": 2}
            }
        ]

        for test_case in test_cases:
            actual_dict = convert_file_to_stemmed_word_count_dict(test_case["text_file_path"], test_case["stop_words"])
            self.assertEqual(actual_dict, test_case["expected_dict"],
                             f'found dict \n{actual_dict} \nnot equal to expected \n{test_case["expected_dict"]}')

class Test_get_top_20_word_count(unittest.TestCase):

    def test_get_top_20_word_count(self):
        test_cases = [
            # an empty input should return an empty list
            {
                "input_dict": {},
                "expected_list": []
            },
            # the output should be in descending order with respect to each key's value
            {
                "input_dict": {"fred": 1, "wilma": 2, "pebbles": 3},
                "expected_list": ["pebbles", "wilma", "fred"]
            },
            # The output should be limited to 20 items
            {
                "input_dict": {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13, 14:14,
                               15:15, 16:16, 17:17, 18:18, 19:19, 20:20, 21:21},
                "expected_list": [21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
            },
            {
                "input_dict": {},
                "expected_list": []
            },
        ]

        for test_case in test_cases:
            ordered_list = get_top_20_word_count(test_case["input_dict"])
            self.assertEqual(ordered_list, test_case["expected_list"])

    # ints and strings can't be compared, so this input breaks the sorting process
    def test_throws_when_mixing_value_types(self):
        mixed_dict = {"number 1":1, "number 2":2, "number 3":3, "string 1":"1", "string 2":"2", "string 3":"3"}
        with self.assertRaises(TypeError):
            get_top_20_word_count(mixed_dict)

if __name__ == "__main__":
    unittest.main()