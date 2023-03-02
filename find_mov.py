import csv
import sys
s = sys.argv[1]
print(s)
with open('D:\Projects\Movie list making\data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Loop over each row in the CSV file and print its contents
    for row in reader:
        if row[0] == s:
            print("\n "+ row[0])
            print("\n "+ row[1])
            print("\n "+ row[2])
            print("\n "+ row[3])


    