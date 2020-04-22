from csv import DictReader
# ordered dictionary
with open('file.csv','r') as f:
    csv_reader = DictReader(f,delimiter = '|') # DictReader function is better that reader function
    for row in csv_reader:
        print(row['email'])