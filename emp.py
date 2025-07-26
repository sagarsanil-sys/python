#!/usr/bin/env python3

import csv
from collections import defaultdict


filess="employees.csv"


dept_sal = defaultdict(int)

with open(filess,"r") as file:
	reader=csv.DictReader(file)
	for row in reader:
		depart= row['Department']
		salary=int(row['Salary'])
		dept_sal[depart]=salary


max_sal = max(dept_sal, key=dept_sal.get)
print(f"Department with highest salary {max_sal} {dept_sal[max_sal]}")
