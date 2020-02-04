import csv
import pandas as pd
f = open('Properties_Receiving_SBR.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
content = list()
property = list()
lst_property = list()
counts = dict()

for line in rdr:
  content = line[6],line[5],line[2]
  property.append(content[1])
#print(property)


print(counts)


for i in property:
  if i not in lst_property:
     lst_property.append(i)
     counts[i] = 1
  else:
    counts[i] += 1
counts = sorted(counts.items(),reverse=True, key=lambda item: item[1])
counts = counts[:20]


df = pd.read_csv('f2019.csv', sep='\t', engine='python')
print(df)


print(lst_property)
print(counts)
f.close()
