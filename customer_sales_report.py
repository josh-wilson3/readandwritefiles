import csv

sales = open('sales.csv', 'r')
outfile = open('salesreport.csv', 'w')

csv_file = csv.reader(sales)

outfile.write(f"Customer ID, Total\n")

next(csv_file)

custid = '250'
total = 0

for rec in csv_file:
    if custid == rec[0]:
        total += float(rec[3]) + float(rec[4]) + float(rec[5])
        
    else:
        #write the customer id, total to the outfile
        outfile.write(f"{rec[0]}, ${total:,.2f}\n")
        custid = rec[0]
        total = float(rec[3]) + float(rec[4]) + float(rec[5])
    
    outfile.write(f"{rec[0]}, ${total:,.2f}\n")

outfile.close()