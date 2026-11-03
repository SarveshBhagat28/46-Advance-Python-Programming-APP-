
import numpy as np
import pandas as pd

# Create book records
books = ["Python", "Java", "C Programming", "Data Science", "DBMS"]
prices = np.array([450, 600, 350, 750, 550])

# Calculate average price
print("Average Book Price:", np.mean(prices))

# Create Pandas DataFrame
df = pd.DataFrame({
    "Book Name": books,
    "Price": prices
})

print("\nBook Records:")
print(df)

# Display books costing more than 500
print("\nBooks costing more than Rs. 500:")
print(df[df["Price"] > 500])
