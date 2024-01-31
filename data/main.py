import csv
import re
from collections import Counter

dates = []

with open('TVILLE.csv', 'r') as f:
   for lines in csv.reader(f):
        if not any(date['date'] == lines[0] for date in dates):
            dates.append({"date": lines[0], "timestamps": []})

        for date in dates:
            if date['date'] == lines[0]:
                date['timestamps'].append(re.split(":", lines[1][0:2], 1)[0] + ":00")

data = {}

for date in dates:
    a = dict(Counter(date['timestamps']))

    if date['date'] != 'date':
        data[date['date']] = a


all_headers = set(header for values in data.values() for header in values.keys())

csv_file_path = 'output.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    csv_writer.writerow(['Date'] + list(all_headers))
    
    for date, values in data.items():
        row = [date] + [values.get(header, 0) for header in all_headers]
        csv_writer.writerow(row)