"""Unit Tests for M4Pro_Webscraping"""

import numpy as np
import pandas as pd
import unittest
from M4Pro_Webscraping_HarleyCoughlin import get_top_chart, write_to_csv


class GetTopChartTest(unittest.TestCase):

    def test_year(self):
        """Ensure that AssertionError gets raised from incorrect year values."""

        with self.assertRaises(AssertionError) as cm:
            get_top_chart("airest")

        with self.assertRaises(AssertionError) as cm:
            get_top_chart(0)

        with self.assertRaises(AssertionError) as cm:
            get_top_chart(-100)

        with self.assertRaises(AssertionError) as cm:
            get_top_chart(2025)

        with self.assertRaises(AssertionError) as cm:
            get_top_chart(1209309183120390)

    def test_earliest_year(self):
        """Test that the earliest year (1946) works correctly."""
        df = get_top_chart(1946)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(len(df) > 0)

    def test_latest_year(self):
        """Test that the latest year (2024) works correctly."""
        df = get_top_chart(2024)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(len(df) > 0)

    def test_dataframe_columns(self):
        """Test that the returned DataFrame has the expected columns."""
        df = get_top_chart(2020)
        self.assertIn("No.", df.columns)
        self.assertIn("Title", df.columns)
        self.assertIn("Artist(s)", df.columns)
        self.assertIn("Year", df.columns)
        self.assertEqual(len(df.columns), 4)

class WriteToCSVTest(unittest.TestCase):

    def test_frames(self):
        """Ensure that AssertionError gets raised from incorrect frames type."""

        with self.assertRaises(AssertionError) as cm:
            frames = None
            write_to_csv(frames)

        with self.assertRaises(AssertionError) as cm:
            frames = 0
            write_to_csv(frames)

        with self.assertRaises(AssertionError) as cm:
            frames = "Arastinoe"
            write_to_csv(frames)

        with self.assertRaises(AssertionError) as cm:
            frames = pd.Series()
            write_to_csv(frames)

    def test_write_works_with_single_dataframe(self):
        """Test that write_to_csv works with a single dataframe."""
        df = get_top_chart(2020)
        write_to_csv([df])
        import os
        self.assertTrue(os.path.exists("top_charts.csv"))

    def test_concat_multiple_years(self):
        """Test that we can concatenate data from multiple years."""
        frames = [get_top_chart(2020), get_top_chart(2021)]
        write_to_csv(frames)

        result = pd.read_csv("top_charts.csv", doublequote=False,
                             escapechar='\\')
        self.assertIn(2020, result["Year"].unique())
        self.assertIn(2021, result["Year"].unique())

    def test_write_to_csv_output_format(self):
        """Test that the CSV file has the correct format."""
        frames = [get_top_chart(2020)]
        write_to_csv(frames)

        result = pd.read_csv("top_charts.csv", doublequote=False,
                             escapechar='\\')
        self.assertEqual(list(result.columns),
                         ["No.", "Title", "Artist(s)", "Year"])
        first_row = result.iloc[0]
        self.assertIsInstance(first_row["No."], (np.int64))
        self.assertIsInstance(first_row["Title"], str)
        self.assertIsInstance(first_row["Artist(s)"], str)
        self.assertIsInstance(first_row["Year"], np.int64)


if __name__ == "__main__":
    unittest.main()
