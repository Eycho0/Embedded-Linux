import re
import csv

with open('port.h', 'r') as headerfile:
    header_content = headerfile.read()

prototypes = re.findall(r'void\s+\w+\s*\(.*\)', header_content)

IDs = re.findall(r'ID\[hex\]:.[a-z0-9]+',header_content)

csv_data = []
for i in zip(prototypes,IDs):
    csv_data.append(i)

with open('function_prototypes.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Function Prototype','Service ID Value'])
    csvwriter.writerows(csv_data)

print("CSV file created successfully.")
