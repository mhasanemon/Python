import openpyxl
import os

os.chdir('c:\\users\\emon\\Downloads')

workbook = openpyxl.load_workbook('example.xlsx')

sheet = workbook.get_sheet_names()
print(sheet)