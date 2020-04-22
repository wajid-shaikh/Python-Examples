# csv - comma separated values
# to store data in tabular formats
from csv import reader
with open('file.csv','r') as f: # f - treated as object
    csv_reader = reader(formats)
    # csv_reader is an iterator
    # print(type(csv_reader))
    next(csv_reader)
    for row in csv_reader:
        print(row)