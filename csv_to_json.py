import csv
import json

csvfile = open("test.csv",'r')
jsonfile = open("test.json",'w')

#this parses through the csv file
reader = csv.DictReader(csvfile)

# this dumps to a JSON file this needs to write to the JSON object for firebase firestore
for row in reader:
    json.dump(row,jsonfile)
    jsonfile.write('\n')