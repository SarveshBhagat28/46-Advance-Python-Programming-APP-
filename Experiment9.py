import csv
import json

with open("input.csv", "r") as file:
    data = list(csv.DictReader(file))

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data converted successfully!")
