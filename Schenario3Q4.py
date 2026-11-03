import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", default="mobiles.csv")
args = parser.parse_args()

with open(args.file, "r") as file:
    reader = csv.DictReader(file)
    mobiles = list(reader)

print("\n--- Mobile Records ---")
for mobile in mobiles:
    print(mobile)

brand = input("\nEnter Brand Name to search: ")

found = False

for mobile in mobiles:
    if mobile["Brand"].lower() == brand.lower():
        print("\nMobile Found:")
        print(mobile)
        found = True

if not found:
    print("No mobile found for this brand!")