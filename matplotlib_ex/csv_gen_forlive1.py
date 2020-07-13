import csv
import random

import time
x_value = 0
total_1 = 1000
total_2 = 1000

fieldname = ['x_val', 'tot_1', 'tot_2']

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldname)
    csv_writer.writeheader()

while True:

    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldname)

        info = {
            'x_val' : x_value,
            'tot_1' : total_1,
            'tot_2' : total_2
        }

        csv_writer.writerow(info)
        print(x_value, total_1, total_2)

        x_value += 1
        total_1 = total_1 + random.randint(-6, 8)
        total_2 = total_2 + random.randint(-5, 6)

    time.sleep(1)

