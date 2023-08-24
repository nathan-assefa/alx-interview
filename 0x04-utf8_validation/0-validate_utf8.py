#!/usr/bin/python3
''' utf-8 validation '''


def validUTF8(data):
    # Initialize a variable to keep track of the number of continuation bytes expected
    num_continuation_bytes = 0

    # Iterate through each integer in the data list
    for byte in data:
        # Check if it's a continuation byte
        if num_continuation_bytes > 0:
            # Check if the byte starts with the pattern "10"
            if (byte >> 6) == 0b10:
                num_continuation_bytes -= 1
            else:
                return False
        else:
            # Check if it's a single-byte character (ASCII)
            if (byte >> 7) == 0:
                continue
            # Check for multi-byte characters
            elif (byte >> 5) == 0b110:
                num_continuation_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_continuation_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_continuation_bytes = 3
            else:
                return False

    return num_continuation_bytes == 0
