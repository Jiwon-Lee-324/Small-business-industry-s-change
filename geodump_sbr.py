import sqlite3
import json
import codecs
import re

conn = sqlite3.connect('sbr_lite.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0

for row in cur :
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue
    a=list()
    if not('status' in js and js['status'] == 'OK') : continue
    i=0
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    a.append(str(js["results"][0]["address_components"]))
 #   print(a)
  #  print(type(a))
    lst = list()
    k=0
    for i in a:
        lst = i.replace(',', '\n,')
      #  print(lst)
        result= lst.find("West Yorkshire")
        if result >0:
            print("\n",i)

      #  print(type(i))
   # for i in a:
      # print(a)
      #  result = re.findall("\s+West Yorkshire\s+",i)
     #   print(result)




    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    #print(type(where))
    try :
      #  print(where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")

