#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""

import sys
import re
from collections import defaultdict

def print_stats(total_size, status_codes):
    """Print accumulated statistics"""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def main():
    """Main function to process log lines and compute metrics"""
    total_size = 0
    line_count = 0
    status_codes = defaultdict(int)
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'

    try:
        for line in sys.stdin:
<<<<<<< Updated upstream
            total_size, status_codes = process_line(
                line, total_size, status_codes)
            line_count += 1

            # Print statistics every 10 lines
            if line_count == 10:
                print_stats(total_size, status_codes)
                line_count = 0  # Reset the counter after 10 lines

=======
            try:
                match = re.match(pattern, line.strip())
                if match:
                    status_code = int(match.group(1))
                    file_size = int(match.group(2))
                    
                    # Update metrics
                    if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                        status_codes[status_code] += 1
                    total_size += file_size
                    line_count += 1

                    # Print stats every 10 lines
                    if line_count % 10 == 0:
                        print_stats(total_size, status_codes)
                        
            except ValueError:
                continue
                
>>>>>>> Stashed changes
    except KeyboardInterrupt:
        # Handle CTRL+C
        print_stats(total_size, status_codes)
        raise

<<<<<<< Updated upstream
    finally:
        # Print final stats after finishing reading input
        if line_count > 0:  # Check if any remaining lines to print
            print_stats(total_size, status_codes)


=======
>>>>>>> Stashed changes
if __name__ == "__main__":
    main() 
