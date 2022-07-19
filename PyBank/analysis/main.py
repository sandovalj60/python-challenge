import os
import csv

budget_csv = os.path.join ("..", "Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv, encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")


    # Read the header row first (skip this part if there is no header)
    # csv_header = next(csv_file) # reads header as a string
    csv_header = next(csv_reader) # reads header as list
    print(f"Header: {csv_header}")