"""Create a csv file from top songs charts on Wikipedia from 1946 to 2024."""
# This program records information apout the top 100 songs for each year
# available on Wikipedia.
# 03/02/2025
# CSC221 M4Pro
# Harley Coughlin


import pandas as pd


def get_top_chart(year):
    """Gets the Year-end list of songs from Wikipedia. Returns a DataFrame.

    Params
    ------
    year
        Year to download the top songs chart from.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the top songs.
    """
    assert isinstance(year, int), f"Expected integer year and got {year}."
    assert 1946 <= year <= 2024, "Expected year between 1946 and 2024."

    print(f"Getting chart for {year}.")
    url = "https://en.wikipedia.org/wiki/" \
          f"Billboard_Year-End_Hot_100_singles_of_{year}"
    tables = pd.read_html(url)
    table_num = 0
    # Ran into an issue with the 2012 page that is registering an extra table
    # on the page in the 0 position. So do a quick check to make sure 'Title'
    # and 'Artist(s)' columns exist. The first couple pages have a different
    # column name for 'No.'
    for i, table in enumerate(tables):
        if "Title" in table.columns and "Artist(s)" in table.columns:
            table_num = i
    table = tables[table_num]
    # Add the year to the dataframe.
    table["Year"] = year
    table.columns = ["No.", "Title", "Artist(s)", "Year"]

    assert isinstance(table, pd.DataFrame)
    amount_columns = len(table.columns)
    assert amount_columns == 4, f"Expected 4 columns got {amount_columns}."

    return table


def write_to_csv(frames):
    """Concatenates DataFrames and writes to a csv file.

    Params
    ------
    frames: list[pd.DataFrame]
        List of dataframes to concatenate and print to csv_file.
    """
    assert frames is not None, "Expected list of dataframes got None."
    assert isinstance(frames, (list, pd.DataFrame)), "Expected frames to be a"\
                                                     " list of DataFrames."

    print("Concatinating the charts.")
    frame = pd.concat(frames)
    assert isinstance(frame, pd.DataFrame), "Expected frame to be a DataFrame."
    # Rename the columns since the first column from the 1946 page is
    # "No. (Rank)" and virtually all the others is just "No."
    print("Writing the csv.")
    # Writing to the csv, not double quoting any quotations and using \ as the
    # escape character.
    frame.to_csv("top_charts.csv", index=False, doublequote=False,
                 escapechar='\\')


def main():
    write_to_csv([get_top_chart(2012)])


def this():
    """Calls get_top_chart for each year from 1946 to 2024."""
    start_year = 1946
    end_year = 2025
    try:
        charts = [get_top_chart(year) for year in range(start_year, end_year)]
        write_to_csv(charts)
    # I'm honestly unsure of what exceptions could be thrown.
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except IndexError as e:
        print(f"IndexError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")


if __name__ == "__main__":
    main()
