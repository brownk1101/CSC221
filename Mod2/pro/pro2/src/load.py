"""Module for creating excel sheets"""


import xlsxwriter
import os.path
import pandas as pd
import transform


def create_excel_sheets(data: pd.DataFrame, name: str) -> None:
    """Writes excel files to resources/output/{name}

    Parameters
    ----------
    data: pd.DataFrame
        DataFrame to write to excel file.
    name: str
        Name of the excel file.
    """
    file_path = os.path.join("resources", "output")
    file_path = os.path.join(file_path, name + ".xlsx")
    data.to_excel(excel_writer=file_path)


def create_option3_sheet(data: pd.DataFrame, division_name: str,
                         course_codes: list[str], headers: list[str]) -> None:
    """Writes a formatted excel file

    Parameters
    ----------
    data: pd.DataFrame
        Division dataframe.
    division_name: str
        Name of the division.
    course_codes: list[str]
        List of unique course codes without section information.
    headers: list[str]
        List of headers to be printed in the first row.
    """
    file_name = division_name.lower() + "_FTE" + ".xlsx"
    file_path = os.path.join("resources", "output")
    file_path = os.path.join(file_path, file_name)

    with xlsxwriter.Workbook(file_path) as workbook:
        worksheet = workbook.add_worksheet()
        # Write the header current_row
        worksheet.write_row(0, 0, headers)

        # Keep track of the current_row that we're on
        current_row = 1

        for course in course_codes:
            course_info = transform.get_course_frame(data, course)
            worksheet.write(current_row, 1, course)
            current_row += 1
            for row in course_info.itertuples(index=False):
                worksheet.write_row(current_row, 2, row)
                current_row += 1
            worksheet.write(current_row, 1, "Total")
            current_row += 1

        worksheet.write(current_row, 1, "Div Total")
        # Try to fit the columns to the widest data available in each column
        worksheet.autofit()
