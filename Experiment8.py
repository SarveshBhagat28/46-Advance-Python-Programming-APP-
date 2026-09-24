
with open("input.txt", "r") as file:
    lines = file.readlines()
print("Number of lines:", len(lines))
first_two = lines[:2]
with open("output.txt", "w") as file:
    file.writelines(first_two)
print("First two lines written to output.txt")
