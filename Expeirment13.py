import threading

def count_numbers():
    for number in range(1, 6):
        print("Number:", number)

def calculate_squares():
    for number in range(1, 6):
        print("Square:", number * number)

def calculate_cubes():
    for number in range(1, 6):
        print("Cube:", number * number * number)

threads = [
    threading.Thread(target=count_numbers),
    threading.Thread(target=calculate_squares),
    threading.Thread(target=calculate_cubes)
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("All threads completed.")
