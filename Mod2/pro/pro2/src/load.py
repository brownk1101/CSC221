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


def create_fte_excel(data: pd.DataFrame, name: str, course_codes: list[str],
                           first_cell: str | None = None ) -> None:
    """Writes a formatted FTE excel file to resources/output/{name}_FTE.xlsx

    Parameters
    ----------
    data: pd.DataFrame
        Division dataframe.
    name: str
        Name of the excel file.
    course_codes: list[str]
        List of unique course codes without section information.
    first_cell: str | None (default = None)
        If not None, the value will be written to the first cell of the sheet.
    """
    filename = name.lower() + "_FTE" + ".xlsx"
    file_path = os.path.join("resources", "output")
    file_path = os.path.join(file_path, filename)

    current_row = 0
    start_column = 1 if first_cell is None else 2

    with xlsxwriter.Workbook(file_path) as workbook:
        worksheet = workbook.add_worksheet()
        # Write the header row.
        if first_cell is not None:
            worksheet.write(current_row, 0, first_cell)
            worksheet.write(current_row, 1, "Course Code")
            worksheet.write_row(0, start_column, data.columns)
        else:
            worksheet.write(current_row, 0, "Course Code")
            worksheet.write_row(0, start_column, data.columns)

        current_row += 1
        # Write the course information.
        for course in course_codes:
            course_info = transform.get_course_frame(data, course)
            # Write the course name to the cell in the column/row before the
            # course information.
            worksheet.write(current_row, start_column - 1, course)
            current_row += 1
            # Write the course information.
            for row in course_info.itertuples(index=False):
                worksheet.write_row(current_row, start_column, row)
                current_row += 1
            # Write total.
            worksheet.write(current_row, start_column - 1, "Total")
            current_row += 1

        # Write div total for division, instructor
        if first_cell is not None:
            worksheet.write(current_row, 1, "Div Total")
        # Try to fit the columns to the data.
        worksheet.autofit()
