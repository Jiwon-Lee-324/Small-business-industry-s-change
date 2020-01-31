import csv
f = open('Properties_Receiving_SBR.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
content = list()
for line in rdr:
  content = line[6],line[5],line[2]
  print(content)
  for i in content:

f.close(