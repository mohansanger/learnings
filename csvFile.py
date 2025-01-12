import csv

file= open(r'C:\Users\Mohan.2.Singh\Downloads\Test PY\Book1.csv','r')
#reader=csv.reader(file)
reader=csv.DictReader(file)
lst=list(reader)
for row in lst:
    print(row)
   
