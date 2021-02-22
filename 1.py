import csv

path = 'output_data.csv'
with open(path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['No', 'Name', 'Score'])
    writer.writerow([1, 'Tom', 87.3])
    writer.writerow([2, 'Mary', 76.4])
    writer.writerow([3, 'Mark', 65.5])