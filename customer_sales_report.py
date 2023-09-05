import csv

sales = open('sales.csv', 'r')
outfile = open('salesreport.csv', 'w')

csv_file = csv.reader(sales)

outfile.write(f"Customer ID, Total\n")

next(csv_file)

for rec in csv_file:
    #print(rec[3], rec[4], rec[5])
    total = float(rec[3]) + float(rec[4]) + float(rec[5])
    
    outfile.write(f"{rec[0]}, ${total:,.2f}\n")

outfile.close()