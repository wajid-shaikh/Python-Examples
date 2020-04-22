# writer , DictWriter
from csv import writer
with open('file.csv','w', newline='') as f:
    csv_writer = writer(f)
    # methods 1. writerow
    #         2. writerows 

    # by writerow ->

    # csv_writer.writerow(['name', 'countries'])
    # csv_writer.writerow(['wajid', 'india'])
    # csv_writer.writerow(['jeff bezos', 'america'])
    # csv_writer.writerow(['vladimir putin', 'russia'])

    # by writerows->
    csv_writer.writerows([['name', 'countries'], ['wajid', 'india'], ['jeff bezos', 'america'], ['vladimir putin', 'russia']])