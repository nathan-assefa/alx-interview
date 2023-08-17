#!/usr/bin/python3

import sys


def print_statistics(status_counts, total_size):
    ''' Printig the statistics '''
    print(f"File size: {total_size}")
    for code, count in sorted(status_counts.items()):
        if count != 0:
            print(f"{code}: {count}")


total_file_size = 0
code = 0
counter = 0
dict_sc = {"200": 0,
           "301": 0,
           "400": 0,
           "401": 0,
           "403": 0,
           "404": 0,
           "405": 0,
           "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if (code in dict_sc.keys()):
                    dict_sc[code] += 1

            if (counter == 10):
                print_statistics(dict_sc, total_file_size)
                counter = 0

finally:
    print_statistics(dict_sc, total_file_size)
