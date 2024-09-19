import sys

# Open the file and read line by line
with open('falselines.txt', 'r') as file:
    for line in file:
        # Print each line to stdout
        sys.stdout.write(line)

