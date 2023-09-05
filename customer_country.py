import csv

customers = open('customers.csv', 'r')
outfile = open('customer_country.csv', 'w')

csv_file = csv.reader(customers)

outfile.write(f'Full name, Country\n')

next(csv_file) #Skips header row

counter = 0

for rec in csv_file:
    outfile.write(f"{rec[1]} {rec[2]}, {rec[4]}\n")
    counter += 1

outfile.close()

print(f"total number of customers: {counter}")