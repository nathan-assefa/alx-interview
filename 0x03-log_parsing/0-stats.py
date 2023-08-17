#!/usr/bin/python3

import sys

def print_statistics(status_counts, total_size):
    ''' Printig the statistics '''
    print("File size: {}".format(total_size))
    for code, count in sorted(status_counts.items()):
        if count != 0:
            print("{}: {}".format(code, count))

def main():
    ''' analysing the log metrics '''
    total_size = 0
    line_counter = 0
    status_counts = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    try:
        for line in sys.stdin:
            parsed_line = line.split()

            if len(parsed_line) <= 10:
                line_counter += 1

                if line_counter <= 10:
                    total_size += int(parsed_line[-1])
                    status_code = parsed_line[-2]

                    if status_code in status_counts:
                        status_counts[status_code] += 1

                if line_counter == 10:
                    print_statistics(status_counts, total_size)
                    line_counter = 0

    finally:
        print_statistics(status_counts, total_size)

if __name__ == "__main__":
    main()
