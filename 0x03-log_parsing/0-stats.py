#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

def print_stats():
    """Prints the computed metrics."""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def signal_handler(sig, frame):
    """Handles keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        
        try:
            # Split the line into components
            parts = line.split()
            if len(parts) < 7:
                continue

            ip_address = parts[0]
            date = parts[3] + " " + parts[4]
            request = parts[5] + " " + parts[6] + " " + parts[7]
            status_code = int(parts[8])
            file_size = int(parts[9])

            # Update total file size
            total_size += file_size

            # Update status code count
            if status_code in status_counts:
                status_counts[status_code] += 1

        except (ValueError, IndexError):
            # If there's a parsing error, skip the line
            continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    # Handle any remaining stats on keyboard interruption
    print_stats()
    sys.exit(0)

# Print final stats if the script ends normally
print_stats()

