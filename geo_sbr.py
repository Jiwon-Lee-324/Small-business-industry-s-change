import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys
import csv
count = 0
content = list()

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"



conn = sqlite3.connect('sbr.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

f = open('f2019.csv', 'r')
rdr = csv.reader(f)

for line in rdr:

    content.append(line[1])
content = content[:100]

for line in content:

    address = line
#    print(address)
  #  print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
                (memoryview(address.encode()),))

    try:
        data = cur.fetchone()[0]
        print("Found in database ", address)
        continue
    except:
        pass

    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

  #  print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
   # print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        #print(data)  # We print in case unicode causes an error
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS'):
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
                VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode())))
    cur.execute('''Delete From Locations (address, geodata)
                VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode())))
    conn.commit()
  #  if count % 10 == 0:
    #    print('Pausing for a bit...')
       # time.sleep(5)

print("Finished")
