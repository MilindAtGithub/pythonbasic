# This is the file which will generate the CSV with column Heading
import csv

with open('test.csv', 'w', newline='') as csvfile:
    fieldnames = ['FirstName', 'LastName', 'LoanNumber']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'FirstName':'Milind','LastName':'Deo', 'LoanNumber':12345})
    writer.writerow({'FirstName': 'Alam', 'LastName': 'FinX', 'LoanNumber': 475474})