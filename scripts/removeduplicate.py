import csv

file1 = "file1.csv"
file2 = "file2.csv"

output = "merged_uniqe.csv"

rows = set()

for file in [file1, file2]:
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.add(tuple(row))
