import csv
import sys

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      if len(row)==3:
        print([float(row[0]),float(row[1]),float(row[2])])
      else:
        print("!=3")
