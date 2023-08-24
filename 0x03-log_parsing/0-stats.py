#!/usr/bin/python3
import sys

""" Anayzing the log entires """


def print_statistics(status_counts, total_size):
    """Printig the statistics"""
    print(f"File size: {total_size}")
    for code, count in sorted(status_counts.items()):
        if count != 0:
            print(f"{code}: {count}")


def main():
    """analysing the log metrics"""
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
        "500": 0,
    }

    try:
        for line in sys.stdin:
            parsed_line = line.split()
            parsed_line.reverse()

            if len(parsed_line) >= 3:
                line_counter += 1

                if line_counter <= 10:
                    total_size += int(parsed_line[0])
                    status_code = parsed_line[1]

                    if status_code in status_counts:
                        status_counts[status_code] += 1

                if line_counter == 10:
                    print_statistics(status_counts, total_size)
                    line_counter = 0

    except KeyboardInterrupt:
        pass

    finally:
        print_statistics(status_counts, total_size)
main()
