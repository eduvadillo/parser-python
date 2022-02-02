import re
import csv
from collections import Counter

def reader_codes(filename):
    with open(filename) as f:
        log = f.read()

        regexp = r'200 | 404|50\d{1}'

        ips_list = re.findall(regexp, log)

        return(ips_list)

def reader_ip(filename):
    with open(filename) as f:
        log = f.read()

        regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

        ips_list = re.findall(regexp, log)

        return(ips_list)

def count_codes(ips_list):
    counter = Counter(ips_list)
    return(counter)

"""
def write_csv(counter):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        header = ['IP', 'Frequency']

        writer.writerow(header)

        for item in counter:
            writer.writerow( (item, counter[item]))

"""

if __name__ == '__main__':
    print("Ejercicio 1: ", count_codes(reader_ip('log')))
    print("Ejercicio 2: ",count_codes(reader_codes('log')))
