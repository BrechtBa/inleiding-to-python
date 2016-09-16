import csv

coord = []
with open('data.csv') as f:
    reader = csv.DictReader(f, delimiter='\t')
    for row in reader:
    	coord.append( (row['x'],row['y'],row['y'],) )

for c in coord:
    print( c )