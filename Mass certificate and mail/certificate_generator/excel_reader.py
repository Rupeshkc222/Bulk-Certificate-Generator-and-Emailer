import openpyxl

def read_names_and_emails_from_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    names_and_emails = []
    for row in sheet.iter_rows( values_only=True):
        name = row[0]
        email = row[1]
        if name and email:
            names_and_emails.append((name, email))
    return names_and_emails
