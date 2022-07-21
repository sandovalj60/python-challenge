# import dependencies

import os
import csv

#path for files to load and output

election_load = os.path.join("..", "Resources", "election_data.csv")
election_output = os.path.join("analysis", "election_analysis.txt")

# open file

with open(election_load) as csv_file:
