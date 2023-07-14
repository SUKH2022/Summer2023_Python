import requests
import json

# Open/Prep CSV
csv_f = open("weatherApi.csv")
csv_raw = csv_f.read()
csv_f.close()
csv = csv_raw.split("\n")

for i in range(len(csv)):
    csv[i] = csv[i].split(',')

# Get weather from API
weatherReports = []
for row in csv:
    reqUrl = f"http://www.7timer.info/bin/api.pl?lon={row[2]}&lat={row[1]}&product=astro&output=json"
    res = requests.get(reqUrl)
    weatherReports.append(json.loads(res.text))

# Create headers for spreadsheet
headerString = ""
headers = []
for header in weatherReports[0]['dataseries'][0]:
    headerString += header + ","
    headers.append(header)
headerString += "\n"

# Build spreadsheet with retrieved data
for i in range(1,len(csv)):
    fname = f"{csv[i][0]}Weather.csv"
    f = open(fname, 'w')
    f.write(headerString)
    for series in weatherReports[i]['dataseries']:
        writeString = ""
        for key in headers:
            writeString += str(series[key]).replace(",","") +","
        writeString += "\n"
        f.write(writeString)
    f.close()

    # Write file name back to first CSV
    csv[i][3] = fname

# Write rebuilt CSV back to file
csv_joinRows = []
for row in csv:
    csv_joinRows.append(','.join(row))
csvRebuilt = "\n".join(csv_joinRows)

csv_f = open("weatherApi.csv", 'w')
csv_f.write(csvRebuilt)
csv_f.close()