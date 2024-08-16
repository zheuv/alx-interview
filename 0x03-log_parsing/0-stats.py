import datetime
import sys
import signal

"""
DOc for script
"""


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


signal.signal(signal.SIGINT, signal_handler)


def checkFileSize(size):
    """Checks if size can be converted to an integer."""
    return can_be_converted_to_int(size)


def checkDate(date):
    """Validates if the date is in the correct format."""
    date = date[0] + " " + date[1]
    if (date[0] == "[") and (date[-1] == "]")
    and can_be_interpreted_as_date(date[1:-1]):
        return True
    return False


def checkGet(get):
    """Checks if the GET request matches the expected format."""
    sentence = ['"GET', '/projects/260', 'HTTP/1.1"']
    return get == sentence


def checkStatusCode(code):
    """Validates if the status code is one of the allowed values."""
    possibleCodes = [200, 301, 400, 401, 403, 404, 405, 500]
    return can_be_converted_to_int(code) and int(code) in possibleCodes


def checkIp(ip):
    """Checks if the IP address is valid."""
    ip = ip.split('.')
    return len(ip) == 4 and
    all(x is True for x in [can_be_converted_to_int(x) for x in ip])


def can_be_interpreted_as_date(date_string):
    """Checks if the string can be interpreted as a date."""
    try:
        datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")
        return True
    except ValueError:
        return False


def can_be_converted_to_int(element):
    """Checks if the element can be converted to an integer."""
    try:
        int(element)
        return True
    except ValueError:
        return False


def checkInput(line):
    """Validates and processes a single input line."""
    if line:
        line = line.split()
        if len(line) == 9:
            if all(x is True for x in [checkIp(line[0]),
                                       checkDate(line[2:4]),
                                       checkGet(line[4:7]),
                                       checkStatusCode(line[7]),
                                       checkFileSize(line[8])]):
                status_counts[int(line[7])] += 1
                global total_size
                total_size += int(line[8])
                return True
    return False


try:
    for line in sys.stdin:
        print(line)
        line_count += 1
        try:
            if line:
                checkInput(line)
        except (ValueError, IndexError):
            continue
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)


print_stats()
