#!/usr/bin/python3
""" utf-8 validation """


def validUTF8(data):
    """
    Validate UTF-8 encoding
    """

    num_continuation_bytes = 0

    for num in data:
        # Convert to 8-bit binary representation
        binary_rep = f"{num:08b}"[-8:]
        if num_continuation_bytes == 0:
            for bit in binary_rep:
                if bit == "0":
                    break
                num_continuation_bytes += 1
            if num_continuation_bytes == 0:
                continue
            if num_continuation_bytes == 1 or num_continuation_bytes > 4:
                return False
        else:
            if not (binary_rep[0] == "1" and binary_rep[1] == "0"):
                return False
        num_continuation_bytes -= 1

    return num_continuation_bytes == 0
