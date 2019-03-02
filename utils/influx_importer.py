#!/usr/bin/python
'''
influx_importer - Import bike count data into InfluxDB time series database
By Garret Rumohr

'''
import argparse
import csv
import json
import datetime
import ipdb
from pprint import pprint
from influxdb import InfluxDBClient


def parse_line(row, dateformat):
    '''
    parse raw bike count line and return parts with python datetime object
    '''
    try:
        int(row[-1:][0])  #last list entry should be a cyle or ped integer val
    except ValueError:
        is_row = False
        entry_date = None
        entry_pedestrians = None
        entry_cycles = None
        return is_row, entry_date, entry_pedestrians, entry_cycles

    '''
    This might have to be an area of data validation improvement
    however, all examples have had Date and time in seprate rows.
    We can combine them into a python datetime object for more flexiblity.
    '''
    parsed_date = datetime.datetime.strptime(str(row[0]) + ' ' \
                                             + str(row[1]), \
                                             dateformat)

    is_row = True
    entry_date = parsed_date.strftime('%Y-%m-%dT%H:%M:%SZ')
    entry_pedestrians = row[2]
    entry_cycles = row[3]

    return is_row, entry_date, entry_pedestrians, entry_cycles


def main(args):
    '''
    read line from csv
    check if in influx DB
    insert if not
    '''
    #make influxDB client
    client = InfluxDBClient(args.influx_server,
                            args.influx_port,
                            args.influx_user,
                            args.influx_password,
                            args.influx_database)
    dateformat = '%d/%m/%Y %H:%M'
    entries = []

    with open(args.file, 'r', newline='') as csv_infile:
        reader = csv.reader(csv_infile)
        for row in reader:
            is_row, entry_date, entry_pedestrians, entry_cycles = parse_line(row, dateformat)
            if is_row:
                #check to see if there is an entry for this time slot.
                query_string = "select value from %s where time='%s';" % (args.influx_database, entry_date)
                precheck_result = client.query(query_string)
                if len(precheck_result) == 0: #if no time entry, lets add one
                        payload = {}
                        payload['measurement'] = args.counter_name
                        payload['time'] = entry_date
                        payload['fields'] = { 'pedestrians': entry_pedestrians, 'bicyclists': entry_cycles }
                        commit = []
                        commit.append(payload)
                        #import ipdb; ipdb.set_trace()
                        client.write_points(commit)
                        pprint(payload)
                else:
                    pprint(precheck_result)
    client.close()
    print("fin!")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Bike Counter InfluxDB importer')
    parser.add_argument('-f','--file', help='Source CSV file',required=True)
    parser.add_argument('-n','--counter-name',help='Counter Name', required=True)
    parser.add_argument('-s','--influx-server',help='InfluxDB host', required=True)
    parser.add_argument('-o','--influx-port',default=8086,help='InfluxDB Port', required=False)
    parser.add_argument('-u','--influx-user',help='InfluxDB username', required=True)
    parser.add_argument('-p','--influx-password',help='InfluxDB password', required=True)
    parser.add_argument('-d','--influx-database',help='InfluxDB BikeCounter DB name', required=False)

    args = parser.parse_args()
    main(args)
