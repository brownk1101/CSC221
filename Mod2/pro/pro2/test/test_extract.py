"""Test suite for extract"""
import unittest
import pandas as pd
from src.extract import extract_csv


class TestExtractionFunctions(unittest.TestCase):

    def test_valid_csv(self):
        df = extract_csv("deansDailyCsar.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)

    def test_none_filename(self):
        with self.assertRaises(AssertionError):
            extract_csv(None)

    def test_empty_filename(self):
        with self.assertRaises(AssertionError):
            extract_csv("")

    def test_wrong_type(self):
        with self.assertRaises(AssertionError):
            extract_csv(123)

    def test_non_csv_file(self):
        with self.assertRaises(AssertionError):
            extract_csv("test.txt")

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            extract_csv("nonexistent.csv")

    def test_empty_csv(self):
        with self.assertRaises(pd.errors.EmptyDataError):
            extract_csv("empty_csv.csv")


if __name__ == "__main__":
    unittest.main()
