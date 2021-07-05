#! /usr/bin/python3

print("content-type: text/html")
print()


print('''<style>
pre{
color: black;
font-weight: bold;
font-size: 20px;
}
</style>''')


import cgi
import subprocess as sb
import requests
import xmltodict
import json

fs = cgi.FieldStorage()

plate_no = fs.getvalue("plate_no")

def get_vehicle_info(plate_no):
    r = requests.get("http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={0}&username=Abhay01".format(str(plate_no)))
    data = xmltodict.parse(r.content)
    jdata = json.dumps(data)
    df = json.loads(jdata)
    df1 = json.loads(df['Vehicle']['vehicleJson'])
    return df1

get_vehicle_info(plate_no)

else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")
