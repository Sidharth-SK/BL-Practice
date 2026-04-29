import csv
"""WORKING WITH CSV"""
with open('file handeling\\practice_csv.csv', 'r') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        print(row)

data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'London']
]

with open('file handeling\\practice_csv.csv', 'a', newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(data)

with open('file handeling\\practice_csv.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)