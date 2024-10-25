#!/usr/bin/python3
import sys


def print_stats(file_size, status_codes):
    """
    Prints the file size and the number of occurrences for each status code.
    """
    print(f"File size: {file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


# Initialize variables
file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        try:
            # Split the line to extract required information
            parts = line.split()
            status_code = int(parts[-2])
            size = int(parts[-1])

            # Update file size
            file_size += size

            # Update status code count if it's valid
            if status_code in status_codes:
                status_codes[status_code] += 1

        except Exception:
            continue  # If the line format is incorrect, skip it

        # Every 10 lines, print statistics
        line_count += 1
        if line_count % 10 == 0:
            print_stats(file_size, status_codes)

except KeyboardInterrupt:
    # Handle CTRL + C by printing the final statistics before exiting
    print_stats(file_size, status_codes)
    sys.exit(0)

# Print final statistics if the script ends naturally
print_stats(file_size, status_codes)

