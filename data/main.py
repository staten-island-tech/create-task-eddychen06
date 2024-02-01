import csv
import re
from collections import Counter

dates = []

with open('TVILLE.csv', 'r') as f:
   for lines in csv.reader(f):
        if not any(date['date'] == lines[5] for date in dates):
            dates.append({"date": lines[5], "detection_hour": []})

        for date in dates:
            if date['date'] == lines[5] and date['date'] != 'date':
                if lines[5] == lines[10][0:8]:
                    date['detection_hour'].append("Hour " + str(int(re.split(":", lines[8][0:2], 1)[0]) + 1))
                else: 
                    date['detection_hour'].append("Hour " + str(int(re.split(":", lines[8][0:2], 1)[0]) + 5))

data = {}

for date in dates:
    a = dict(Counter(date['detection_hour']))

    if date['date'] != 'date':
        data[date['date']] = a

print(data)

all_headers = list(set(header for values in data.values() for header in values.keys()))


all_headers = sorted(all_headers, key = lambda x : x[-2:])

csv_file_path = 'output.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    
    csv_writer.writerow(['Date'] + list(all_headers))
    
    for date, values in data.items():
        row = [date] + [values.get(header, 0) for header in all_headers]
        csv_writer.writerow(row)
