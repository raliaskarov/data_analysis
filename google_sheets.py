# set of functions to communicate with google sheets

import gspread
from google.colab import auth
from google.auth import default
import gspread_dataframe as gd
from gspread_dataframe import set_with_dataframe

# function to read single cell from google sheets
def read_google_sheet_cell(workbook_id, worksheet_name, cell):
    # Connect to Google Sheets file
    workbook = gc.open_by_key(workbook_id)

    # Reach sheet
    worksheet = workbook.worksheet(worksheet_name)

    # Read the value of the specified cell
    cell_value = worksheet.acell(cell).value  # 'acell' returns the cell at 'cell' address
    return cell_value


def write_to_google_sheet(workbook_id, worksheet_name, df):
    # connect to google sheets file
    workbook = gc.open_by_key(workbook_id)

    # reach sheet
    worksheet = workbook.worksheet(worksheet_name)

    # Clear the existing worksheet content
    worksheet.clear()

    # Write the DataFrame to the worksheet
    set_with_dataframe(worksheet, df)

def write_string_to_google_sheet_cell(workbook_id, worksheet_name, cell, string_value):
    # Connect to Google Sheets file
    workbook = gc.open_by_key(workbook_id)

    # Reach sheet
    worksheet = workbook.worksheet(worksheet_name)

    # Write the string value to the specified cell
    worksheet.update(cell, string_value)
