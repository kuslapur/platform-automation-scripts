import csv

data = [
    ["Name", "Age", "City"],
    ["Ravi", 30, "Bangalore"],
    ["Anita", 25, "Mysore"],
    ["Kiran", 28, "Hyderabad"]
]

with open("report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("Report generated successfully as 'report.csv'")



