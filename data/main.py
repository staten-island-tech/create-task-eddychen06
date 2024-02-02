from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd
import csv
import re

dates = []

with open('SITHS.csv', 'r') as f:
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

all_headers = list(set(header for values in data.values() for header in values.keys()))
all_headers = sorted(all_headers, key = lambda x : x[-2:])

with open('output.csv', 'w', newline='') as f:
    csv_writer = csv.writer(f)
    
    csv_writer.writerow(['Date'] + list(all_headers))

    x = []
    y = ['Date'] + list(all_headers)
    
    for date, values in data.items():
        row = [date] + [values.get(header, 0) for header in all_headers]
        x.append(row)
        csv_writer.writerow(row)

df = pd.DataFrame(x,columns=y)
df.plot(x='Date', kind='bar', stacked=True,
        title='Hourly Calls for SITHS Site')
plt.show()