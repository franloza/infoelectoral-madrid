import sys
with open(sys.argv[1], "r") as a_file:
    for line in a_file:
        print(line.strip()
              .replace(u'\u00AD', ' '))