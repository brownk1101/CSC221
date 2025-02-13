"""Module for creating excel sheets"""


import os.path


def create_excel_sheets(data, name: str) -> None:
    """Writes excel files to resources/output/"""
    file_path = os.path.join("resources", "output")
    file_path = os.path.join(file_path, name + ".xlsx")
    data.to_excel(excel_writer=file_path)
