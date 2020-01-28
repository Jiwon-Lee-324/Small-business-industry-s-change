import csv
f = open('Properties_Receiving_SBR.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
  print(line)
f.close()