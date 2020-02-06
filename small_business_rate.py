import csv
import matplotlib.pyplot as xyz

f = open('f2019.csv', 'r')
rdr = csv.reader(f)
content = list()
property = list()
lst_property = list()
counts = dict()

for line in rdr:
    content = line[6],line[5],line[2]
    property.append(content[1])
print(type(property))

for i in property:
    i = i.replace(' and Premises', '')
    i = i.replace(' And Premises', '')
    if i not in lst_property:
        lst_property.append(i)
        counts[i] = 1
    else:
        counts[i] += 1
counts = sorted(counts.items(),reverse=True, key=lambda item: item[1])

counts = counts[:20]


for key,val in counts:
    xyz.barh(key,val)
xyz.ylabel('Industry')

xyz.show()

f.close()
