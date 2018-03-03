#!/usr/bin/python
'''
redate - Date conversion utility
read in bikecounter csv and mangle the date into the format
provided by the args or default.

Built with Python 3.6 in mind
By Garret Rumohr

'''
import argparse
import csv
import datetime
import ipdb

def main(args):
    entries = []
    if args.date:
        dateformat = str(args.datetime)
    else:
        dateformat = '%d/%m/%Y %H:%M'
    with open(args.file, 'r', newline='') as csv_infile:
        reader = csv.reader(csv_infile)
        for row in reader:
            entries.append(row)

    outries = []
    outries.append(['Date', 'Pedestrian', 'Cyclists'])
    toss_it = entries.pop(0) #pull the header off the list.
                             #probably a bad assumption and should test.
    for entry in entries:
        parsed_date = datetime.datetime.strptime(str(entry[0]) + ' ' \
                                                 + str(entry[1]), \
                                                 dateformat)
        outries.append([parsed_date, entry[2], entry[3]])

    with open(args.output, 'w', newline='') as csv_outfile:
        writer = csv.writer(csv_outfile)
        writer.writerows(outries)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Bike Counter date mangler')
    parser.add_argument('-f','--file', help='Source CSV file',required=True)
    parser.add_argument('-o','--output',help='Ouput CSV file', required=True)
    parser.add_argument('-d','--date',help='Date Format', required=False)
    args = parser.parse_args()
    main(args)
