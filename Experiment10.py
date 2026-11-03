import numpy as np

arr = np.arange(1, 11)

print("Original Array:", arr)

print("\n--- Array Creation ---")
print("Zeros:", np.zeros(5))
print("Ones:", np.ones(5))
print("Empty:", np.empty(3))
print("Range:", np.arange(2, 10, 2))
print("Linspace:", np.linspace(0, 10, 5))

x = np.ones(5, dtype=np.int64)
print("Integer Array:", x)

print("\n--- Slicing ---")
print("First 5 Elements:", arr[:5])
print("Last 5 Elements:", arr[5:])
print("Elements from index 2 to 6:", arr[2:7])
print("Every Second Element:", arr[::2])

print("\n--- Statistical Operations ---")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

print("\n--- Broadcasting ---")
print("Original Array:", arr)
print("Array + 5:", arr + 5)
print("Array * 2:", arr * 2)

print("\n--- Sorting ---")
unsorted = np.array([5, 2, 8, 1, 9, 3])
print("Original:", unsorted)
print("Sorted:", np.sort(unsorted))

print("\n--- Concatenation ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Combined Array:", np.concatenate((a, b)))

print("\n--- Mathematical Operations ---")
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Element-wise Multiplication:\n", A * B)
print("Matrix Multiplication:\n", A @ B)
