
import numpy as np
import pandas as pd

# Create student records
names = ["Amit", "Rahul", "Sneha", "Priya", "Rohan"]
marks = np.array([85, 72, 92, 65, 88])

# Calculate statistics
print("Mean Marks:", np.mean(marks))
print("Median Marks:", np.median(marks))
print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))

# Create Pandas DataFrame
df = pd.DataFrame({
    "Student Name": names,
    "Marks": marks
})

print("\nStudent Records:")
print(df)

# Display students scoring more than 80
print("\nStudents scoring more than 80 marks:")
print(df[df["Marks"] > 80])
