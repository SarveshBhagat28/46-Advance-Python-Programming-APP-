import re

text = input("Enter a text: ")

pattern = r'\b[A-Za-z0-9._-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,4}\b'

emails = re.findall(pattern, text)

print("\n--- Using findall() ---")
if emails:
    for email in emails:
        print(email)
else:
    print("No email addresses found.")

print("\n--- Using search() ---")
match = re.search(pattern, text)

if match:
    print("First email:", match.group())
    print("Position:", match.span())
    print("Original String:", match.string)
    print("Matched Text:", match.group())
else:
    print("No match found.")

print("\n--- Using split() ---")
words = re.split(r'\s+', text)
print("Split text:", words)

print("\n--- Using sub() ---")
modified_text = re.sub(pattern, "[EMAIL]", text)
print("Modified text:", modified_text)
